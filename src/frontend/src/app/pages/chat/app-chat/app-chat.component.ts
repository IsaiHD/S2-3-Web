import { Component } from '@angular/core';

@Component({
  selector: 'app-chat',
  templateUrl: './app-chat.component.html',
  styleUrl: './app-chat.component.scss'
})
export class AppChatComponent {
  newMessageText: string = '';
  messages: { text: string, isUser: boolean }[] = [];

  sendMessage() {
    if (this.newMessageText.trim()) {
      this.messages.push({ text: this.newMessageText, isUser: true });
      this.newMessageText = '';
    }
  }
}
