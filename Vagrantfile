Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y git python3-pip
      pip3 install django
      pip3 install django-cors-headers
      pip3 install python-social-auth[django]
      git clone https://github.com/jbyra/super-zwierzaki.git ~/super-zwierzaki
      cd ~/super-zwierzaki/super_zwierzaki
      python3 manage.py makemigrations app
      python3 manage.py migrate
      python3 manage.py runserver 0:8585&
    SHELL
end

