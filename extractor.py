import cv2
import numpy as np
np.set_printoptions(suppress=True)

from skimage.measure import ransac
from skimage.transform import FundamentalMatrixTransform
from skimage.transform import EssentialMatrixTransform


# turn [[x,y]] -> [[x,y,1]]
def add_ones(x):
    return np.concatenate([x, np.ones((x.shape[0], 1))], axis=1)

f_est_avg = []

class Extractor(object):
    def __init__(self, K):
        self.orb = cv2.ORB_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        self.last = None
        self.K = K
        self.Kinv = np.linalg.inv(self.K)

    def normalize(self, pts):
        return np.dot(self.Kinv, add_ones(pts).T).T[:, 0:2]

    def denormalize(self, pt):
        ret = np.dot(self.K, np.array([pt[0], pt[1], 1.0]))
        #ret /= ret[2]
        return int(round(ret[0])), int(round(ret[1]))

    def extract(self, img):
        # detection
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=9)

        # extraction
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=10) for f in feats]
        kps, des = self.orb.compute(img, kps)

        # matching
        ret = []
        if self.last is not None:
            matches = self.bf.knnMatch(des, self.last['des'], k=2)
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    kp1 = kps[m.queryIdx].pt
                    kp2 = self.last['kps'][m.trainIdx].pt
                    ret.append((kp1, kp2))
        # filter
        if len(ret) > 0:
            ret = np.array(ret)

            # normalize coords
            ret[:, 0, :] = self.normalize(ret[:, 0, :])
            ret[:, 1, :] = self.normalize(ret[:, 1, :])

            model, inliers = ransac((ret[:, 0], ret[:, 1]),
									EssentialMatrixTransform,
									#FundamentalMatrixTransform,
									min_samples=8,
                                    #residual_threshold=1,
									residual_threshold=0.005,
									max_trials=100)
        #print (sum(inliers), len(inliers))
            ret = ret[inliers]

            W = np.mat([[0,-1,0],[1,0,0],[0,0,1]],dtype=float)
            u,d,vt = np.linalg.svd(model.params)
            assert np.linalg.det(u) > 0
            if np.linalg.det(vt) < 0:
                 vt *= -1.0
            R = np.dot(np.dot(u, W), vt)
            if np.sum(R.diagonal()) < 0:
                R = np.dot(np.dot(u, W.T), vt)
            print(R)


        # return
        self.last = {'kps': kps, 'des': des}
        return ret