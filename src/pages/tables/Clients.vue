<script setup>
import CustomHeader from "@/components/CustomHeader.vue";
</script>

<template>
	<div id="page-wrapper">
		<!-- Header -->
		<header>
			<CustomHeader active-page="clients" />
		</header>
		<main>
			<div class="container mt-5">
				<h2 class="mb-4">Destinations Management</h2>
				<div class="table-container">
					<table class="table table-striped table-bordered">
						<thead class="table-dark">
							<tr>
								<th>#</th>
								<th>Destination</th>
								<th>Country</th>
								<th>Price</th>
								<th>Actions</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>1</td>
								<td>Paris</td>
								<td>France</td>
								<td>$1500</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>
							<tr>
								<td>2</td>
								<td>Tokyo</td>
								<td>Japan</td>
								<td>$1800</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>

							<tr>
								<td>3</td>
								<td>Sydney</td>
								<td>Australia</td>
								<td>$2000</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>
							<tr>
								<td>4</td>
								<td>New York</td>
								<td>USA</td>
								<td>$2500</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>
							<tr>
								<td>5</td>
								<td>London</td>
								<td>UK</td>
								<td>$2200</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>
							<tr>
								<td>6</td>
								<td>Rome</td>
								<td>Italy</td>
								<td>$1700</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>
							<tr>
								<td>7</td>
								<td>Dubai</td>
								<td>UAE</td>
								<td>$3000</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>
							<tr>
								<td>8</td>
								<td>Bangkok</td>
								<td>Thailand</td>
								<td>$1600</td>
								<td>
									<div class="btn-group btn-responsive">
										<button
											class="btn btn-outline-primary btn-sm"
										>
											<i class="fas fa-eye"></i>
										</button>
										<button
											class="btn btn-outline-warning btn-sm"
										>
											<i class="fas fa-edit"></i>
										</button>
										<button
											class="btn btn-outline-danger btn-sm"
										>
											<i class="fas fa-trash"></i>
										</button>
									</div>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</main>

		<footer class="bg-dark text-center text-light p-3">
			<p>&copy; 2024 Tunik & Shvets co.</p>
			<div class="footer-icons">
				<a href="tel:+123456789" class="mr-3"
					><i class="fas fa-phone"></i
				></a>
				<a href="mailto:r.shvetsss@gmail.com" class="mr-3"
					><i class="fas fa-envelope"></i
				></a>
				<a href="https://t.me/tearsalloverthefloor" class="mr-3"
					><i class="fab fa-telegram"></i
				></a>
				<a href="https://wa.me/380670123456" class="mr-3"
					><i class="fab fa-whatsapp"></i
				></a>
			</div>
		</footer>
	</div>

	<!-- Модальне вікно Авторизації -->
	<div
		class="modal fade"
		id="loginModal"
		tabindex="-1"
		role="dialog"
		aria-labelledby="loginModalTitle"
		aria-hidden="true"
	>
		<div class="modal-dialog" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="loginModalTitle">
						Форма Авторизації
					</h5>
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
					<form>
						<div class="form-group">
							<label for="emailLogin">Email</label>
							<input
								type="email"
								class="form-control"
								id="emailLogin"
								placeholder="Enter email"
							/>
						</div>
						<div class="form-group">
							<label for="passwordLogin">Password</label>
							<input
								type="password"
								class="form-control"
								id="passwordLogin"
								placeholder="Password"
							/>
						</div>
						<button type="submit" class="btn btn-primary">
							Login
						</button>
					</form>
				</div>
			</div>
		</div>
	</div>

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
