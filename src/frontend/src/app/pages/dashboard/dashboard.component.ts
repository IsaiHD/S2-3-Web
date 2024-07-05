import { Component, ViewChild, ViewEncapsulation } from '@angular/core';
import { ChartComponent } from 'ng-apexcharts';
import { productsData } from './models';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  encapsulation: ViewEncapsulation.None,
  styleUrls: ['./dashboard.component.css'] 
})
export class AppDashboardComponent {
  @ViewChild('chart') chart: ChartComponent = Object.create(null);

  public profitExpanceChart: any; 
  public trafficChart: any; 
  public salesChart: any; 

  displayedColumns: string[] = ['profile', 'hrate', 'exclasses', 'status'];
  dataSource: productsData[] = []; 

  constructor() {

  }
}
