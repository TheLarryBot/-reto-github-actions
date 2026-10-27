# Reto: CI/CD con GitHub Actions

Workflow de integración continua que ejecuta `pytest` en cada push a `main`
(y en pull requests hacia `main`). Si las pruebas pasan, un segundo job
revisa el estilo del código con ruff.

## Experimentos

- **A – Éxito:** push del código correcto → las 3 pruebas pasan (check verde en Actions).
- **B – Fallo:** `estado()` modificada para devolver siempre `"Aprobado"`:
  `test_reprobado` falla con `AssertionError: assert 'Aprobado' == 'Reprobado'`
  (`estado(2.5)` debía devolver `"Reprobado"`). El step *Ejecutar pruebas* queda en rojo
  y el job `lint` no se ejecuta.

## Reflexión

Una prueba fallida indica que el comportamiento de la aplicación ya no cumple lo
especificado. Llevar esa versión a producción expone a los usuarios a errores
(en este caso, estudiantes reprobados que aparecerían como aprobados), con costos
mayores de corrección, pérdida de confianza y posibles consecuencias legales o
económicas. El pipeline actúa como compuerta de calidad automática: solo el
código verificado avanza.
