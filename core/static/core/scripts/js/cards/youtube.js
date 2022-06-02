var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var i = 0;

function onYouTubeIframeAPIReady() {
    let containerFront = document.getElementById("front");
    let containerBack = document.getElementById("back");

    if (containerFront) {
        youtubeInsert(containerFront);
    }

    if (containerBack) {
        youtubeInsert(containerBack);
    }

    let containersMark = document.getElementsByClassName('markdownx-preview');

    for (const container of containersMark) {
        setInterval(() => youtubeInsert(container), 1000);
    }
}

function youtubeInsert(container) {
    let re = /({{ [^\s]+?((watch\?v=)([a-zA-Z0-9_-]+)?|(youtu.be\/)([a-zA-Z0-9_-]+)?|(youtube.com\/embed)([a-zA-Z0-9_-]+)?)[^\s]+? }})/g
    let result = re.exec(container.innerHTML);

    while (result != null) {
        let videoID = result[0].replaceAll('}', '').replaceAll('{', '').replaceAll(' ', '');
        videoID = videoID.split('/').slice(-1)[0];
        videoID = videoID.split('?').slice(-1)[0];
        videoID = videoID.split('=').slice(-1)[0];

        container.innerHTML = container.innerHTML.replace(result[0], `<div id="player-${i}"></div>`);

        new YT.Player(`player-${i}`, {
            height: '360',
            width: '640',
            videoId: videoID,
        });

        i++;

        result = re.exec(container.innerHTML);
    }
}
