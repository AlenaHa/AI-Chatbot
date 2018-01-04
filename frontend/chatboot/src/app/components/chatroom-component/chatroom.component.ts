import { Component, OnChanges } from '@angular/core';
import { MessageComponent } from '../message-component/message.component';
import { ChatroomMessageListService } from './chatroom-message-list.service';

@Component({
  selector: 'app-chatroom',
  templateUrl: './chatroom.component.html',
  styleUrls: ['./chatroom.component.scss'],
  providers: [ChatroomMessageListService]
})
export class ChatroomComponent implements OnChanges{
  private message: string;
  private textValue: string;
  
  constructor(private messageListService: ChatroomMessageListService){}

  ngOnChanges(): void {
    this.messageListService.getMessageList();
  }

  public addMessage(): void {
    this.message = this.textValue;
    this.textValue = "";
    this.messageListService.addMessage(this.message);
    this.messageListService.getMessageList();    
  }
}
