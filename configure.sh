#!/bin/bash
# Create and fill configuration file .env.
read -p "Input administrator name (uses to enter admin panel): " ADMINISTRATOR_NAME
read -p "Input administrator password (uses to enter admin panel): " ADMINISTRATOR_PASSWORD
read -p "Input administrator e-mail (target to send reports about completed quizzes): " ADMINISTRATOR_EMAIL
read -p "Input hostname of post server: " POST_SERVER_NAME
read -p "Input server port for send and receive e-mail: " POST_SERVER_PORT
read -p "Input mailbox of quiz system (source of send reports about completed quizzes): " SERVICE_MAILBOX
read -p "Input mailbox password of quiz system: " SERVICE_MAILBOX_PASSWORD
read -p "Input name of admin panel [Ковалева А.]: " ADMIN_PANEL_NAME
ADMIN_PANEL_NAME=${ADMIN_PANEL_NAME:-"Ковалева А."}
read -p "Input password of admin panel: " ADMIN_PANEL_PASSWORD

echo SECRET_KEY=\"$(python -c "from random import choice; result = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]); print(result);")\" > .env
echo DEBUG=1 >> .env
echo ALLOWED_HOSTS=\""*"\" >> .env
echo "" >> .env
echo ADMINISTRATOR_NAME=\"$ADMINISTRATOR_NAME\" >> .env
echo ADMINISTRATOR_PASSWORD=\"$ADMINISTRATOR_PASSWORD\" >> .env
echo ADMINISTRATOR_EMAIL=\"$ADMINISTRATOR_EMAIL\" >> .env
echo "" >> .env
echo POST_SERVER_NAME=\"$POST_SERVER_NAME\" >> .env
echo POST_SERVER_PORT=$POST_SERVER_PORT >> .env
echo SERVICE_MAILBOX=\"$SERVICE_MAILBOX\" >> .env
echo SERVICE_MAILBOX_PASSWORD=\"$SERVICE_MAILBOX_PASSWORD\" >> .env
echo "" >> .env
echo ADMIN_PANEL_NAME=\"$ADMIN_PANEL_NAME\" >> .env
echo ADMIN_PANEL_PASSWORD=\"$ADMIN_PANEL_PASSWORD\" >> .env