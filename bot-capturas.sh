#!/usr/bin/bash
# Script para correr el bot de capturas
# nohup es un comando que permite que el proceso siga corriendo aunque se cierre la terminal y & es para que se ejecute en segundo plano
# La ruta del archivo run_bot.py debe ser el path absoluto
# El path por defecto es $HOME/Documents/bot-capturas-ceic/run_bot.py, pero puede ser cambiado por el path absoluto del archivo

nohup python $HOME/Documents/bot-capturas-ceic/run_bot.py &
