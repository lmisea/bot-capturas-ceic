# Bot de telegram del CEIC para recibir capturas

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-orange?style=for-the-badge&logo=Python)](https://www.python.org/)
![Love](https://img.shields.io/badge/Made%20with-Love-pink?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+R2l0SHViIFNwb25zb3JzIGljb248L3RpdGxlPjxwYXRoIGQ9Ik0xNy42MjUgMS40OTljLTIuMzIgMC00LjM1NCAxLjIwMy01LjYyNSAzLjAzLTEuMjcxLTEuODI3LTMuMzA1LTMuMDMtNS42MjUtMy4wM0MzLjEyOSAxLjQ5OSAwIDQuMjUzIDAgOC4yNDljMCA0LjI3NSAzLjA2OCA3Ljg0NyA1LjgyOCAxMC4yMjdhMzMuMTQgMzMuMTQgMCAwIDAgNS42MTYgMy44NzZsLjAyOC4wMTcuMDA4LjAwMy0uMDAxLjAwM2MuMTYzLjA4NS4zNDIuMTI2LjUyMS4xMjUuMTc5LjAwMS4zNTgtLjA0MS41MjEtLjEyNWwtLjAwMS0uMDAzLjAwOC0uMDAzLjAyOC0uMDE3YTMzLjE0IDMzLjE0IDAgMCAwIDUuNjE2LTMuODc2QzIwLjkzMiAxNi4wOTYgMjQgMTIuNTI0IDI0IDguMjQ5YzAtMy45OTYtMy4xMjktNi43NS02LjM3NS02Ljc1em0tLjkxOSAxNS4yNzVhMzAuNzY2IDMwLjc2NiAwIDAgMS00LjcwMyAzLjMxNmwtLjAwNC0uMDAyLS4wMDQuMDAyYTMwLjk1NSAzMC45NTUgMCAwIDEtNC43MDMtMy4zMTZjLTIuNjc3LTIuMzA3LTUuMDQ3LTUuMjk4LTUuMDQ3LTguNTIzIDAtMi43NTQgMi4xMjEtNC41IDQuMTI1LTQuNSAyLjA2IDAgMy45MTQgMS40NzkgNC41NDQgMy42ODQuMTQzLjQ5NS41OTYuNzk3IDEuMDg2Ljc5Ni40OS4wMDEuOTQzLS4zMDIgMS4wODUtLjc5Ni42My0yLjIwNSAyLjQ4NC0zLjY4NCA0LjU0NC0zLjY4NCAyLjAwNCAwIDQuMTI1IDEuNzQ2IDQuMTI1IDQuNSAwIDMuMjI1LTIuMzcgNi4yMTYtNS4wNDggOC41MjN6Ii8+PC9zdmc+)
![Smyles](https://img.shields.io/badge/Makes%20people-Smyle-cyan?style=for-the-badge)

Este bot de telegram tiene la intención de facilitar el control y registro de los pagos, **reenviando los comprobantes de pago al grupo de Tesorería.**
En un futuro se le podrían añadir más funcionalidades, como por ejemplo, registrar los pagos en un drive, o en el mismo Excel de control de ventas.

Los archivos de log se guardan en el directorio _$HOME/Documents/bot-capturas-log_, con el nombre del archivo en el formato: _DD-MM-YYYY_HH:MM:SS.log_.
Así, se crea un archivo de log por cada ejecución del bot.

Versión de Python usada a la hora de programar el bot: **3.11.3**

## ¿Cómo correr el Bot?

Es bastante fácil: primero se clona el repositorio, luego se instalan las dependecias y por último se corre el archivo [_run_bot.py_](https://github.com/lmisea/bot-capturas-ceic/blob/main/run_bot.py).

### Primer paso: Clonar el repositorio

Se abre una terminal en el directorio donde se quiera tener el bot para poder hostearlo, y se clona este repo:

```sh
git clone https://github.com/lmisea/bot-capturas-ceic.git
```

### Segundo paso: Instalar las dependecias

Este bot usa la librería **_python-telegram-bot_** en la versión 20.3, que se encuentra bajo la licencia [GNU General Public License v3.0](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/LICENSE). Cabe destacar que hay que estar atento a la hora de buscar documentación, porque en internet sale mucha información de versiones anteriores de la librería, que no son compatibles.

Repositorio de GitHub de la librería: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

**¿Cómo instalar las dependencias?** Se abre una terminal en la carpeta donde se haya clonado el repositorio y simplemente se ejecuta:

```sh
pip install -r requirements.txt
```

Esto instalará la versión exacta de la librería que se usó para este proyecto, por lo que no debería haber ningún problema.

### Tercer paso: Correr el bot

Se abre una terminal en la carpeta donde se haya clonado el repositorio y luego de haber instalado las dependencias, simplemente se ejecuta el archivo [_run_bot.py_](https://github.com/lmisea/bot-capturas-ceic/blob/main/run_bot.py) con Python:

```sh
python run_bot.py
```
