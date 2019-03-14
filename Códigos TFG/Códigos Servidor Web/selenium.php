
<html>
<head><title>TFG</title>
  <!-- VENDOR CSS -->
	<link rel="stylesheet" href="assets/vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" href="assets/vendor/font-awesome/css/font-awesome.min.css">
	<link rel="stylesheet" href="assets/vendor/linearicons/style.css">
	<!-- MAIN CSS -->
	<link rel="stylesheet" href="assets/css/main.css">
	<!-- FOR DEMO PURPOSES ONLY. You should remove this in your project -->
	<link rel="stylesheet" href="assets/css/demo.css">
	<script src="jquery-3.3.1.min.js"></script>
	<!-- GOOGLE FONTS -->
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700" rel="stylesheet">
	<!-- ICONS -->
</head>
<body>
  <script>



  function loadHistory(){
     var parametros = {
                "source" : 1
     };

     $.ajax({
               data: parametros,
               url:   'getHistory.php',
               type:  'POST',
               beforeSend: function () {
               },
               success:  function (response) {
                    var histo = document.getElementById('historyy');
                    histo.innerHTML = response;

                   },
                   ////////  en caso de error

                   error: function(xhr, textStatus, error){
                       console.log(xhr.statusText);
                       console.log(textStatus);
                       console.log(error);
                   }
       });
    }
    window.setInterval(function(){
    loadHistory();
  }, 1000);
  </script>
	<nav class="navbar navbar-default navbar-fixed-top">
		<div class="brand">
			<a href="index.html"><b>TFG</b></a>
		</div>
		<div class="container-fluid">
			<div class="navbar-btn">
				<button type="button" class="btn-toggle-fullwidth"><i class="lnr lnr-arrow-left-circle"></i></button>
			</div>
		<!--	<form class="navbar-form navbar-left">
				<div class="input-group">
					<input type="text" value="" class="form-control" placeholder="Buscar...">
					<span class="input-group-btn"><button type="button" class="btn btn-primary">Buscar</button></span>
				</div>
			</form>-->
			<div id="navbar-menu">
				<ul class="nav navbar-nav navbar-right">
				<!--	<li class="dropdown">
						<a href="#" class="dropdown-toggle icon-menu" data-toggle="dropdown">
							<i class="lnr lnr-alarm"></i>
							<span class="badge bg-danger">5</span>
						</a>
						<ul class="dropdown-menu notifications">
							<li><a href="#" class="notification-item"><span class="dot bg-warning"></span>System space is almost full</a></li>
							<li><a href="#" class="notification-item"><span class="dot bg-danger"></span>You have 9 unfinished tasks</a></li>
							<li><a href="#" class="notification-item"><span class="dot bg-success"></span>Monthly report is available</a></li>
							<li><a href="#" class="notification-item"><span class="dot bg-warning"></span>Weekly meeting in 1 hour</a></li>
							<li><a href="#" class="notification-item"><span class="dot bg-success"></span>Your request has been approved</a></li>
							<li><a href="#" class="more">See all notifications</a></li>
						</ul>
					</li>-->

					<!-- <li>
						<a class="update-pro" href="https://www.themeineed.com/downloads/klorofil-pro-bootstrap-admin-dashboard-template/?utm_source=klorofil&utm_medium=template&utm_campaign=KlorofilPro" title="Upgrade to Pro" target="_blank"><i class="fa fa-rocket"></i> <span>UPGRADE TO PRO</span></a>
					</li> -->
				</ul>
			</div>
		</div>
	</nav>
  <div id="wrapper">
		<div id="sidebar-nav" class="sidebar">
			<div class="sidebar-scroll">
				<nav>
					<ul class="nav">
						<li><a href="index.php"><i class="lnr lnr-home"></i> <span>Inicio</span></a></li>
						<li ><a href="selenium.php" class="active" style="cursor:pointer;" class=""><i class="fa fa-firefox"></i> <span>Selenium</span></a></li>
						<li ><a href="webcam.php" style="cursor:pointer;" class=""><i class="fa fa-camera"></i> <span>WebCam</span></a></li>
					</ul>
				</nav>
			</div>
		</div>
    <div class="main">
      <!-- MAIN CONTENT -->
      <div class="main-content">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-12">
              <div class="panel panel-headline">
                <div class="panel-heading">
                  <h1 class="panel-title"><b><font color="blue">Selenium</font></b></h1>
                  <p class="panel-subtitle">Información captada por el módulo Selenium, así como su historial de registro.</p>
                </div>
                <div class="panel-body">
                  <img id="stream" src="http://localhost:8080/stream?topic=/output_selenium">
                  <br>
                  <h2>Log:</h2>
                 <span id ="historyy"></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
