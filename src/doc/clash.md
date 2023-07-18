services:
    clash:
        image: dreamacro/clash    
        container_name: clash
        volumes:
        - .:/root/.config/clash
        ports:
        - "7890:7890"
        - "7891:7891"
        restart: unless-stopped
        network_mode: "bridge"

docker pull dreamacro/clash
docker run --name Clash -d -v .:/home/htc/Document/clash/config --network="bridge" --privileged dreamacro/clash

docker run -p 20080:80 -d --name yacd --rm ghcr.io/haishanh/yacd:master