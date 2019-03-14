<?php
  define("VIDEO_FILE", "/home/daniel/catkin_ws/src/tfg/record_videos");

  $enlace = mysqli_connect('localhost', 'root', '','tfg_record');

  if (!$enlace) {
      echo "Error: No se pudo conectar a MySQL." . PHP_EOL;
      echo "errno de depuración: " . mysqli_connect_errno() . PHP_EOL;
      echo "error de depuración: " . mysqli_connect_error() . PHP_EOL;
      exit;
  }

if($_POST['source'] == 0)
  $source = 0;
else if($_POST['source'] == 1)
  $source = 1;
else
  $source = 2;

$log_sql = "SELECT * FROM log WHERE source = '".$source."' ORDER BY time DESC ";
$result = mysqli_query($enlace, $log_sql);
$print_log = "";
if (mysqli_num_rows($result) > 0) {
    $print_log .= "<table class=\"table table-hover\">";
    $print_log .= "<tr><th>Fecha</th><th>Información</th></tr>";
   while($log = mysqli_fetch_assoc($result)) {
     if($log['type'] == '0')
       $url_video = "<a href=\"record_videos/".$log['time'].".mp4\">Visualizar</a>";
     else
       $url_video = "";

     $print_log .= "<tr><td>".$log['time']."</td><td>".$log['message']."</td><td>".$url_video."</td></tr>";
    }
	$print_log .= "</table>";
}else{
      $print_log .= "<font color=red><b>No hay registros!.</b></font>";
}
echo $print_log;

?>
