### EXAMEN 2  
**Nombre:** Miguel Andrés Isaza Barona  
**Código:** A00054628  
**Materia:** Sistemas operacionales  
**Correo personal:** miguel11andres@hotmail.com  
**URL repositorio:** https://github.com/DonMiguelin/so-exam2.git

### 3 Instalación y configuración de zsh y git  

-Para la instalación de git se usa el siguiente comando: ``# apt-get install git``  
![](Imagenes/git.png)  

-Para la instalación de zsh se usa el siguiente comando: ``# apt-get install zsh``  
![](Imagenes/Instalación%20zsh.png)  

-Para la instalación de Oh-my-zsh se ejecuta el siguiente comando: ``sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"``  
![](Imagenes/Instalación%20Oh%20my%20zsh.png)  

-Para poder usar oh-my-zsh en cualquier otro usuario (en este caso operativos) se usa el siguiente comando:  
``export ZSH="$HOME/.dotfiles/oh-my-zsh"; sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"``  
Luego de eso oh-my-zsh quedará listo para su uso:  
![](Imagenes/Oh_my-zsh-userOperativos.png)  

-Aquí se muestra la edición de los plugins:  
![](Imagenes/plugins%20autosuggestion.png)  

-Luego de generar el token de acuerdo a la guía en https://github.com/ICESI/so-git/tree/master/00_github_intro, cuando hacemos el git clone por medio de comandos, en la url del repositorio cambia de la siguiente forma: ``~git clone https://xxxxxxxxxxxxxxxxxxxx@github.com/DonMiguelin/so-exam2.git`` (siendo x el valor del token), esto permite que cuando hagamos push por medio de comandos no sea necesario ingresar de nuevo el nombre de usuario y la contraseña, como se muestra en la siguiente imagen:  
![](Imagenes/comandos%20git.png)  
![](Imagenes/Creación%20carpeta.png)  
![](Imagenes/edicion%20README.png)  

### 4 Instalación y configuración del plugin zsh-autosuggestions  

-Para la instalación de este plugin, se ejecuta el comando ``git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions``  
![](Imagenes/Clonando%20plugin%20autosuggestion.png)  

-Luego ``source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh`` esto para ejecutar los cambios que tenga el archivo zsh-autosuggestions.zsh, para editarlo se ejecuta ``~/.zsh/zsh-autosuggestions`` y una vez estemos ahí ejecutamos ``nano zsh-autosuggestions.zsh``  
![](Imagenes/archivo%20a%20configurar.png)  

-Para cambiar el color de resaltado nos vamos a la siguiente línea y cambiamos el valor 8 por yellow:  
![](Imagenes/Cambio%20de%20color%20resaltado.png)  
-Volvemos a ejecutar ``source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh`` y observamos los cambios:  
![](Imagenes/cambios_resaltadoAmarillo.png)  
![](Imagenes/colorAmarillo_2docomando.png)  

### 5 Instalación y configuración de tmux  
-Instalamos tmux mediante el siguiente comando: ``~ apt-get install tmux -y``:  
![](Imagenes/Instalación%20tmux.png)  

-Luego corremos tmux mediante el comando ``~ tmux`` y debe aparecer lo siguiente:  
![](Imagenes/corriendo%20tmux.png)  

-Desde esa sesión, configuramos el archivo tmux.conf para dejar como prefijo la combinación de teclas ctrl + a:  
![](Imagenes/configuraciones%20tmux.png)  

-Para ejecutar esos cambios sin necesidad de reiniciar tmux, solo basta presionar ``ctrl+b`` y luego ``R``  
![](Imagenes/ctrl+R.png)  

-Una ves hecho esto podremos hacer todas las funcionalidades de tmux con ``crtl+a``.  
-Para activar el modo vi, primero debemos instalarlo mediante el comando ``~ apt-get install vim``  
![](Imagenes/instalacion%20vim.png)  


-Para activar este modo usamos ``ctrl+a [`` y podremos navegar a través del buffer:  
![](Imagenes/Modo%20vi.png)  
![](Imagenes/Modo%20vi%203.png)  

-Para usar el modo copia visual al portapapeles, solo debemos presionar espacio y movernos con las felchas para resaltar lo que queremos copiar:  
![](Imagenes/Modo%20vi%202.png)  

-También se puede usar enter para copiar y ``ctrl+a ]`` para pegar la selección.  

### 6 Sesion tmux de nombre so-exam2  

-Nueva sesión y división de pantalla:  
![](Imagenes/nueva%20sesion%20tmux.png)  
![](Imagenes/Division%20pantalla.png)  


-Salida del comando top:  
![](Imagenes/comando%20top.png)  

-Peticiones por medio de curl a cada endpoint. Salida formateada con jq:  
-Instalando jq:  
![](Imagenes/instalando%20jq.png)  

-Creación de courses.py:  
![](Imagenes/coursesPy.png)  

-Salida de la ejecución del script de python courses.py, peticiones curl y salida jq:  
![](Imagenes/curl_jq_1.png)  
![](Imagenes/curl_jq_2.png)  
![](Imagenes/curl_jq_3.png)  
![](Imagenes/curl_jq_4.png)  

-Salida de la ejecución de telnet towel.blinkenlights.nl:  
![](Imagenes/telnet2.png)  
![](Imagenes/telnet3.png)  
![](Imagenes/telnet4.png)  
![](Imagenes/telnet5.png)  

### 7 Aplicación en background y resultados en slack  



