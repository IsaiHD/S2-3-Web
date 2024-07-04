import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { MaterialModule } from '../../material.module'; // Import MaterialModule

import { AppChatComponent } from './app-chat/app-chat.component'; // Import the component

// icons
import { TablerIconsModule } from 'angular-tabler-icons';
import * as TablerIcons from 'angular-tabler-icons/icons';

import { SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';


@NgModule({
  declarations: [
    AppChatComponent, // Declare the component
  ],
  imports: [
      CommonModule,
      FormsModule, // Add FormsModule
      MaterialModule, // Add comma here
      TablerIconsModule.pick(TablerIcons),
      SweetAlert2Module,
    ],
})
export class ChatModule { }
