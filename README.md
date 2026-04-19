# S.L.A.M. v2 🗺️

Pipeline de **SLAM Visual Monocular** em Python — mapeamento e localização simultâneos a partir de um único vídeo ou webcam.

Desenvolvido originalmente para o estágio Scuba Team / Alura, com aplicação potencial em projetos de acessibilidade como o **Lysa (Cão-Guia Robô)**.

---

## O que foi implementado na v2

| Feature | v1 (original) | v2 |
|---|---|---|
| Detecção de features (ORB) | ✅ | ✅ |
| Matching + Lowe's ratio test | ✅ | ✅ |
| RANSAC Essential Matrix | ✅ | ✅ |
| Extração de rotação **R** | ✅ | ✅ |
| Extração de translação **t** | ❌ | ✅ |
| Acumulação de pose da câmera | ❌ | ✅ |
| Triangulação de pontos 3D | ❌ | ✅ |
| Mapa esparso 3D | ❌ | ✅ |
| Visualização 3D (trajetória + mapa) | ❌ | ✅ |
| Suporte a webcam | ❌ | ✅ |
| HUD com estatísticas em tempo real | ❌ | ✅ |

---

## Instalação

```bash
git clone https://github.com/cyb3r-h0bbit/Slam-Alura.git
cd Slam-Alura
pip install -r requirements.txt
```

---

## Uso

```bash
# Rodar com vídeo de teste
python slam.py --video test_countryroad.mp4

# Rodar com webcam
python slam.py --cam 0

# Sem visualização 3D (mais leve, para máquinas limitadas)
python slam.py --video test_countryroad.mp4 --no3d
```

Pressione **Q** para encerrar.

---

## Estrutura do projeto

```
slam_alura_v2/
├── slam.py          # Pipeline principal — loop de vídeo e orquestração
├── extractor.py     # Detecção, descrição, matching e decomposição R|t
├── map.py           # Estrutura de dados: Frame, Map, triangulação
├── display.py       # Display2D (OpenCV) e Display3D (matplotlib, thread)
└── requirements.txt
```

---

## Próximos passos (Fase 3)

- [ ] **Calibração real da câmera** com `cv2.calibrateCamera` para maior precisão
- [ ] **Loop closure** — detectar quando a câmera retorna a um local já visitado
- [ ] **Bundle Adjustment** com g2o ou GTSAM para otimizar o mapa globalmente
- [ ] **SuperPoint / ORB-SLAM3** como backend de features para ambientes com pouca textura (calçadas, corredores)
- [ ] **Detecção de obstáculos** integrada ao mapa 3D para o caso de uso do Lysa

---

## Referências

- [Monocular Visual Odometry — Geiger et al.](https://www.cvlibs.net/publications/Geiger2011IV.pdf)
- [OpenCV Camera Calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
- [twitchslam — geohot](https://github.com/geohot/twitchslam) (inspiração original)
