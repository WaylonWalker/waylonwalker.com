document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".is-collapsible").forEach(collapsible => {
        collapsible.addEventListener("click", function () {
            this.classList.toggle("collapsible-closed");
            this.classList.toggle("collapsible-open");
        });
    });
});

  document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector("#post-body .carousel");
    let scrollAmount = 0;
    let step = 300; // Adjust step size based on item width
    let delay = 2000; // Delay in milliseconds

    function autoScroll() {
      if (carousel) {
        carousel.scrollBy({ left: step, behavior: "smooth" });

        // Loop back when reaching the end
        if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth) {
          setTimeout(() => carousel.scrollTo({ left: 0, behavior: "smooth" }), delay);
        }
      }
    }

    setInterval(autoScroll, delay);
  });
