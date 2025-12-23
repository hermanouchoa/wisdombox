# Utilizo esse Dockerfile, em conjunto com o arquivo docker-compose.yml, para projetos em Laravel
# Deve-se substituir "nome_projeto" pelo nome real do projeto

# Use uma imagem base oficial do PHP 8
FROM php:8.2-apache

# Atualize os pacotes e instale as extensões PHP necessárias
RUN apt-get update && apt-get install -y \
    libicu-dev \
    libzip-dev \
    && docker-php-ext-install -j$(nproc) intl zip pdo pdo_mysql

# Configure o Apache para usar a pasta /var/www/html como raiz do servidor
ENV APACHE_DOCUMENT_ROOT /var/www/html
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# Habilitar o módulo Apache rewrite
RUN a2enmod rewrite

# Exponha a porta 80 do Apache
EXPOSE 80

# Copie o seu código PHP para o diretório de trabalho
COPY . /var/www/nome_projeto/
RUN chmod -R 777 /var/www/nome_projeto/storage \
    chmod -R 777 /var/www/nome_projeto/bootstrap \
    chmod -R 777 /var/www/nome_projeto/public

# Defina o diretório de trabalho para /var/www/html
WORKDIR /var/www/html

# Criando link na html com a public do laravel
RUN ln -s /var/www/nome_projeto/public nome_projeto

# Crie um arquivo info.php na pasta /var/www/html
RUN echo "<?php phpinfo(); ?>" > /var/www/html/info.php

# Inicie o Apache quando o contêiner for executado
CMD ["apache2-foreground"]
