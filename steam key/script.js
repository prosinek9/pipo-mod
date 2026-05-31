function startLoading() {
    document.getElementById('loadingArea').style.display = 'block';
    let progress = document.getElementById('progress');
    let width = 0;
    
    // 10 dakika = 600,000 milisaniye. 100 parçaya bölüyoruz (her 6 saniyede bir artış).
    let interval = setInterval(() => {
        if (width >= 100) {
            clearInterval(interval);
            document.getElementById('status').innerText = "Yükleme tamamlandı! Steam hesabınıza girebilirsiniz.";
        } else {
            width++;
            progress.style.width = width + '%';
        }
    }, 6000); 
}