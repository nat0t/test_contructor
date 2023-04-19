#!/bin/bash
# Create and fill configuration file .env.
read -p "Input administrator name (uses to enter admin panel): " ADMINISTRATOR_NAME
read -p "Input administrator password (uses to enter admin panel): " ADMINISTRATOR_PASSWORD
read -p "Input administrator e-mail (target to send reports about completed quizzes): " ADMINISTRATOR_MAILBOX

read -p "Input name of admin panel [Ковалева А.]: " ADMIN_PANEL_NAME
ADMIN_PANEL_NAME=${ADMIN_PANEL_NAME:-"Ковалева А."}
read -p "Input password of admin panel: " ADMIN_PANEL_PASSWORD

read -p "Input hostname of post server: " EMAIL_HOST
read -p "Input server port for send and receive e-mail: " EMAIL_PORT
read -p "Input mailbox of quiz system (source of send reports about completed quizzes): " SERVICE_MAILBOX
read -p "Input mailbox password of quiz system: " SERVICE_MAILBOX_PASSWORD

echo SECRET_KEY=\"$(python -c "from random import choice; result = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]); print(result);")\" > .env
echo DEBUG=1 >> .env
echo ALLOWED_HOSTS=\""*"\" >> .env
echo "" >> .env
echo ADMINISTRATOR_NAME=\"$ADMINISTRATOR_NAME\" >> .env
echo ADMINISTRATOR_PASSWORD=\"$ADMINISTRATOR_PASSWORD\" >> .env
echo ADMINISTRATOR_MAILBOX=\"$ADMINISTRATOR_MAILBOX\" >> .env
echo "" >> .env
echo ADMIN_PANEL_NAME=\"$ADMIN_PANEL_NAME\" >> .env
echo ADMIN_PANEL_PASSWORD=\"$ADMIN_PANEL_PASSWORD\" >> .env
echo "" >> .env
echo EMAIL_HOST=\"$EMAIL_HOST\" >> .env
echo EMAIL_PORT=$EMAIL_PORT\" >> .env
echo EMAIL_HOST_USER=\"$EMAIL_HOST_USER\" >> .env
echo EMAIL_HOST_PASSWORD=\"$EMAIL_HOST_PASSWORD\" >> .env