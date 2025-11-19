# Recommender System — Personalized Product Recommender

**Proyecto:** Sistema de recomendación personalizado basado en filtrado colaborativo usando la librería `surprise`.

**Descripción corta**
Este repositorio contiene un pipeline modular para entrenar, evaluar y desplegar modelos de recomendación basados en las valoraciones de usuarios. Está pensado como un proyecto de portfolio para demostrar competencia en ingeniería de datos y machine learning aplicada a sistemas de recomendación.

---

## Estructura del repositorio
- `data/` — Indicaciones y carpetas para datos (no se incluyen datos privados).
- `notebooks/` — Notebook profesional con análisis y experimentos.
- `src/` — Código modular: carga de datos, entrenamiento, selección de modelo y generación de recomendaciones.
- `models/` — Modelos entrenados (opcional).
- `requirements.txt` — Dependencias del proyecto.
- `.gitignore` — Archivos y carpetas ignoradas por Git.

---

## Cómo usar (resumen)
1. Coloca los datos en `data/raw/` (CSV con columnas `userId`, `itemId`, `rating`).
2. Instala dependencias: `pip install -r requirements.txt`.
3. Ejecuta `src/model_training.py` para entrenar y guardar un modelo (o usa el notebook en `notebooks/`).
4. Usa `src/recommendation_engine.py` para generar recomendaciones por usuario.

---

## Quick English summary
Personalized recommender pipeline using collaborative filtering (Surprise). Clean project structure ready for GitHub and portfolio.
