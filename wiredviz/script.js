$(document).ready(function () {
    var slideshow = $("#slideshow");
    var coverLeft = $("#cover-left");
    var infoCover = $("#info-cover");
    var images = [];
    var currentIndex = -1;
    var pauseSlideshow = false;
    var baseUrl = "https://raw.githubusercontent.com/federicobiggio/federicobiggio.github.io/main/wiredviz/";

    // Function to load CSV file and images
    function loadImages() {
        $.get(baseUrl + "wired_data.csv", function (data) {
            var lines = data.split("\n");

            // Parse the CSV file
            for (var i = 1; i < lines.length; i++) {
                var parts = lines[i].split(";");
                if (parts.length >= 2) {
                    var imageName = parts[1].trim();
                    var wordsContent = parts[5].trim();

                    images.push({
                        filename: parts[1],
                        year: parts[2],
                        month: parts[3],
                        words: wordsContent
                    });
                }
            }

            // Add images to the slideshow container
            for (var i = 0; i < images.length; i++) {
                var imageElement = $("<div class='slide-image'><img src='" + baseUrl + "wired_cover/" + images[i].filename + "'></div>");
                slideshow.append(imageElement);
            }

            // Display a random image in the cover-left
            showRandomImage();
            showWordsForCurrentImage();
        });
    }

    // Function to display the content of the "words" column in the cover-right
    function showWordsForCurrentImage() {
        if (images.length > 0 && currentIndex >= 0 && currentIndex < images.length) {
            var currentImage = images[currentIndex];
            var wordsContent = currentImage.words;

            // Display the content of the "words" column in the cover-right as an <h3> element
            $("#cover-right").html("<h3>" + wordsContent + "</h3>");
        }
    }

    // Event handler for mouse enter and leave on the slideshow container
    slideshow.on("mouseenter", function () {
        pauseSlideshow = true;
    });

    slideshow.on("mouseleave", function () {
        pauseSlideshow = false;
    });

    // Check if the slideshow should be paused or not in the animateSlideshow function
    function animateSlideshow() {
        if (!pauseSlideshow) {
            // Your slideshow animation code goes here
        }
    }

    // Function to display the current image in the cover-left
    function showCurrentImage() {
        if (images.length > 0) {
            var currentImage = images[currentIndex];

            // Display the image in the cover-left
            var imageSrc = baseUrl + "wired_cover/" + currentImage.filename;
            coverLeft.empty().append("<img src='" + imageSrc + "' style='width: 100%;'>");

            // Display the month and year
            var monthYear = currentImage.month + ", " + currentImage.year;
            infoCover.find("#month-year-info").text(monthYear);

            // Reset the width of images in the slideshow container
            slideshow.find(".slide-image img").css("width", "5px");

            // Display the content of the "words" column in the cover-right
            var wordsContent = currentImage.words;
            $("#cover-right").text(wordsContent);
        }
    }

    // Function to display a random image in the cover-left
    function showRandomImage() {
        if (images.length > 0) {
            var randomIndex = Math.floor(Math.random() * images.length);
            currentIndex = randomIndex;
            var randomImage = images[randomIndex].filename;
            var imageSrc = baseUrl + "wired_cover/" + randomImage;

            coverLeft.empty().append("<img src='" + imageSrc + "' style='width: 100%;'>");

            // Display the month and year
            var currentImage = images[randomIndex];
            var monthYear = currentImage.month + ", " + currentImage.year;
            infoCover.find("#month-year-info").text(monthYear);

            // Display the content of the "words" column in the cover-right
            var wordsContent = currentImage.words;
            $("#cover-right").text(wordsContent);
        }
        showWordsForCurrentImage();
    }

    // Event handler for clicking on a slide image
    slideshow.on("click", ".slide-image", function () {
        var clickedImage = $(this);

        // Reset the width of previous images
        slideshow.find(".slide-image img").css("width", "5px");

        // Set the width of the clicked image
        clickedImage.find("img").css("width", "100px");

        // Display the clicked image at 100% in the "cover-left" div
        var imageSrc = clickedImage.find("img").attr("src");
        coverLeft.empty().append("<img src='" + imageSrc + "' style='width: 100%;'>");

        // Find the index of the clicked image and update currentIndex
        currentIndex = slideshow.find(".slide-image").index(clickedImage);

        // Display the month and year of the clicked image
        var clickedImageInfo = images[currentIndex];
        var monthYear = clickedImageInfo.month + ", " + clickedImageInfo.year;
        infoCover.find("#month-year-info").text(monthYear);

        // Display the content in the cover-right div
        showWordsForCurrentImage();
    });

    // Function to handle hover on an image
    slideshow.on("mouseenter", ".slide-image", function () {
        var hoveredImage = $(this);
        hoveredImage.find("img").css("width", "100px");
    });

    // Function to handle mouse leave on an image
    slideshow.on("mouseleave", ".slide-image", function () {
        var hoveredImage = $(this);
        if (hoveredImage.find("img").css("width") !== "100px") {
            hoveredImage.find("img").css("width", "5px");
        }
    });

    // Handle click on the left arrow
    $("#left-arrow").click(function () {
        if (currentIndex > 0) {
            currentIndex--;
            showCurrentImage();
            showWordsForCurrentImage();
        }
    });

    // Handle click on the right arrow
    $("#right-arrow").click(function () {
        if (currentIndex < images.length - 1) {
            currentIndex++;
            showCurrentImage();
            showWordsForCurrentImage();
        }
    });

    // Display the current image in the cover-left on page load
    loadImages();
});
