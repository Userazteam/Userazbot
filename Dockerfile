# Faster & Secure & Special Container #
# Thanks to mkaraniya & zakaryan2004

FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/Userazteam/Userazbot /root/Userazbot
WORKDIR /root/Userazbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
