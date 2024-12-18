<template>
	<div id="page-wrapper">
		<!-- Header -->
		<header>
			<CustomHeader active-page="home" />
      <AuthorizationModal
      :visible.sync="showAuthorizationModal"
      activePage="home"
    />
		</header>
		<!-- Main Content -->
		<main>
			<!-- Слайдер -->
			<div
				id="carouselExampleSlidesOnly"
				class="carousel slide"
				data-ride="carousel"
			>
				<div class="carousel-inner">
					<div class="carousel-item active">
						<img
							class="d-block w-100"
							src="https://www.puredestinations.co.uk/wp-content/uploads/2016/06/top-10-honeymoon-resorts-honeymoon-packages-1600x400.jpg"
							alt="First slide"
						/>
					</div>
					<div class="carousel-item">
						<img
							class="d-block w-100"
							src="https://www.smartertravel.com/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2023/07/Alaska-mountains-landscape-nature-background-in-autumn-fall-season.-Snow-peaks-banner-panorama.png.webp"
							alt="Second slide"
						/>
					</div>
					<div class="carousel-item">
						<img
							class="d-block w-100"
							src="https://www.oliverstravels.com/uploads/herder_image/_1800-1800_Alpe_D_Huez.png"
							alt="Third slide"
						/>
					</div>
				</div>

				<!-- Кнопки для навігації -->
				<a
					class="carousel-control-prev"
					href="#carouselExampleSlidesOnly"
					role="button"
					data-slide="prev"
				>
					<span
						class="carousel-control-prev-icon"
						aria-hidden="true"
					></span>
					<span class="sr-only">Previous</span>
				</a>
				<a
					class="carousel-control-next"
					href="#carouselExampleSlidesOnly"
					role="button"
					data-slide="next"
				>
					<span
						class="carousel-control-next-icon"
						aria-hidden="true"
					></span>
					<span class="sr-only">Next</span>
				</a>
			</div>

			<!-- Про проект -->
			<section class="about mt-5">
				<div class="container">
					<h2>About Our CRM</h2>
					<p>
						Our Tour Agency CRM is designed to streamline your
						travel business operations. With a user-friendly
						interface and comprehensive features, it allows you to
						manage clients, bookings, and payments efficiently. Our
						platform also offers real-time analytics and reporting,
						so you always have a clear view of your business
						performance. We are committed to helping your travel
						agency grow and thrive with our reliable and scalable
						CRM solution.
					</p>
				</div>
			</section>

			<!-- Відгуки -->
			<section class="reviews mt-5">
				<div class="container">
					<h2 class="text-center">Customer Reviews</h2>
					<div class="row mt-4">
						<div class="col-lg-4 col-md-6 mb-4">
							<div class="card h-100">
								<div class="card-body">
									<h5 class="card-title">John Doe</h5>
									<h6 class="card-subtitle mb-2 text-muted">
										"Excellent Service!"
									</h6>
									<p class="card-text">
										I had an amazing experience with this
										agency. The staff was professional, and
										they helped me plan a perfect vacation.
										Highly recommended!
									</p>
								</div>
								<div class="card-footer">★★★★★</div>
							</div>
						</div>
						<div class="col-lg-4 col-md-6 mb-4">
							<div class="card h-100">
								<div class="card-body">
									<h5 class="card-title">Jane Smith</h5>
									<h6 class="card-subtitle mb-2 text-muted">
										"Seamless Experience!"
									</h6>
									<p class="card-text">
										The CRM was easy to use, and it made
										managing my travel business so much
										easier. The customer support team is
										always ready to help. Great job!
									</p>
								</div>
								<div class="card-footer">★★★★★</div>
							</div>
						</div>
						<div class="col-lg-4 col-md-6 mb-4">
							<div class="card h-100">
								<div class="card-body">
									<h5 class="card-title">Emily Johnson</h5>
									<h6 class="card-subtitle mb-2 text-muted">
										"Highly Recommended!"
									</h6>
									<p class="card-text">
										This CRM is a game-changer for travel
										agencies. It helped me keep track of all
										my bookings and customer interactions
										effortlessly.
									</p>
								</div>
								<div class="card-footer">★★★★★</div>
							</div>
						</div>
					</div>
					<div class="loader-wrapper">
						<div class="lds-ellipsis">
							<div></div>
							<div></div>
							<div></div>
							<div></div>
						</div>
					</div>
				</div>
			</section>

			<!-- Контакти -->
			<section class="contact mt-5">
				<div class="container">
					<h2>Contact Us</h2>
					<p><strong>Phone:</strong> +123 456 789</p>
					<p><strong>Email:</strong> info@touragencycrm.com</p>
					<p><strong>Location:</strong> 123, Main Street, City</p>
				</div>
			</section>
		</main>

		<!-- Footer -->
		<footer>
	<CustomFooter active-page="home" />
		</footer>
	</div>

	<!-- Модальні вікна -->

	<!-- Ваш компонент модального вікна -->

	<!-- Модальне вікно FAQ -->
	<div
		class="modal fade"
		id="faqModal"
		tabindex="-1"
		role="dialog"
		aria-labelledby="faqModalTitle"
		aria-hidden="true"
	>
		<div class="modal-dialog" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="faqModalTitle">FAQ</h5>
					<button
						type="button"
						class="close"
						data-dismiss="modal"
						aria-label="Close"
					>
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<p><strong>1. Як користуватися CRM?</strong></p>
					<p>
						Наша CRM розроблена для зручності управління клієнтами,
						бронюванням та аналітикою в реальному часі.
					</p>
					<p><strong>2. Чи є підтримка клієнтів?</strong></p>
					<p>
						Так, наша підтримка клієнтів доступна 24/7 через телефон
						або електронну пошту.
					</p>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
import { ref } from "vue";
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import AuthorizationModal from "@/components/AuthorizationModal.vue";

export default {
  components: {
    CustomHeader,
    CustomFooter,
    AuthorizationModal,
  },
  setup() {
    const showAuthorizationModal = ref(false); // Керування видимістю модального вікна

    return { showAuthorizationModal };
  },
};
</script>
