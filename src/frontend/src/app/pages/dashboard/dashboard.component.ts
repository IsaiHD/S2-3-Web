import { Component, ViewChild, ViewEncapsulation } from '@angular/core';
import { ChartComponent } from 'ng-apexcharts';
import { productsData } from './models'; // Asegúrate de importar tus modelos

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  encapsulation: ViewEncapsulation.None,
  styleUrls: ['./dashboard.component.css'] // Ajusta la ruta si tienes un archivo de estilos separado
})
export class AppDashboardComponent {
  @ViewChild('chart') chart: ChartComponent = Object.create(null);

  public profitExpanceChart: any; // Ajusta el tipo según tus definiciones
  public trafficChart: any; // Ajusta el tipo según tus definiciones
  public salesChart: any; // Ajusta el tipo según tus definiciones

  displayedColumns: string[] = ['profile', 'hrate', 'exclasses', 'status'];
  dataSource: productsData[] = []; // Ajusta el tipo según tus definiciones y datos

  constructor() {
    // Aquí configurarías tus gráficos y datos como lo tienes en tu código original
    // Se omite la configuración de gráficos y datos para brevedad
  }
}
