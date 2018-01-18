.. _dezvoltare:

Dezvoltare
==========

Pentru a dezvolta AI-Chatbot, trebuie urmati toti pasii descrisi pe pagina de
README.


Structura proiect
-----------------

- **AI-Chatbot/**             -> directorul parinte de proiect
    - **bin/**                -> aici se gasesc executabilele ce trebuiesc rulate
    - **docs/**               -> folderul cu documentatie
    - **etc/**                -> configurari
    - **res/**                -> resurse si alte date
    - **cbot/**               -> pachetul principal pe post de biblioteca
    - **frontend/**           -> interfata aplicatiei
    - **drafts/**             -> diverse scripturi si materiale de cercetare
    - **tests/**              -> teste ce verifica varii functionalitati din aplicatie
    - **requirements.txt**    -> cerintele minime ce trebuiesc instalate (pachete Python)
    - **setup.bat**           -> instaleaza automat pe Windows
    - **setup.py**            -> fisierul de instalare a bibliotecii `cbot`
    - **setup.sh**            -> instaleaza automat pe Linux
    - **TODO**                -> ce ne mai ramane de facut
    - **run[-debug].sh/bat**  -> porneste serverul (in debug mode) pe Windows/Linux

.. _api:

API definitions
---------------

cbot
++++

.. automodule:: cbot
    :members:

cbot.core
+++++++++

.. automodule:: cbot.core
    :members:

cbot.core.chatbot
+++++++++++++++++

.. automodule:: cbot.core.chatbot
    :members:

cbot.core.crawler
+++++++++++++++++

.. automodule:: cbot.core.crawler
    :members:

cbot.models
+++++++++++

.. automodule:: cbot.models
    :members:

cbot.schemas
++++++++++++

.. automodule:: cbot.schemas
    :members:

cbot.views
++++++++++

.. automodule:: cbot.views
    :members:

cbot.views.api
++++++++++++++

.. automodule:: cbot.views.api
    :members:

cbot.views.api.base
+++++++++++++++++++

.. automodule:: cbot.views.api.base
    :members:

cbot.views.api.chat
+++++++++++++++++++

.. automodule:: cbot.views.api.chat
    :members:

cbot.views.api.profiles
+++++++++++++++++++++++

.. automodule:: cbot.views.api.profiles
    :members:

cbot.views.sockio
+++++++++++++++++

.. automodule:: cbot.views.sockio
    :members:

cbot.config
+++++++++++

.. automodule:: cbot.config
    :members:

cbot.settings
+++++++++++++

.. automodule:: cbot.settings
    :members:

cbot.utils
++++++++++

.. automodule:: cbot.utils
    :members:
