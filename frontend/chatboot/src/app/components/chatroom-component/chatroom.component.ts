import { Component, OnChanges, OnInit, OnDestroy } from '@angular/core';
import { MessageComponent } from '../message-component/message.component';
import { ChatroomMessageListService } from './chatroom-message-list.service';
import { Message } from '../../models/message.model';
import { ChatService } from './chatroom-socket.service';


@Component({
  selector: 'app-chatroom',
  templateUrl: './chatroom.component.html',
  styleUrls: ['./chatroom.component.scss'],
  providers: [ChatService, ChatroomMessageListService]
})

export class ChatroomComponent implements OnChanges, OnInit{
  private connection;
  private message:Message;
  private textValue: string;

  constructor(private chatService: ChatService, private messageListService: ChatroomMessageListService) {
        this.connection = this.chatService.getMessages().subscribe(msg => {
        var msgString = msg.toString();
        this.message = new Message(msgString, "bot");
        this.messageListService.addMessage(this.message);
        this.messageListService.getMessageList();
    });
  }

  chat() {
    this.message = new Message(this.textValue, "human");
    this.chatService.sendMessage(this.message.text);
    this.messageListService.addMessage(this.message);
    this.textValue ="";
    this.messageListService.getMessageList();
  }

  handleKeyDown(event : any):void {
    if(event.keyCode == 13) {
      this.chat();
    }
  }

  ngOnChanges(): void {
      this.messageListService.getMessageList();
  }

  ngOnInit() {
  }

  ngOnDestroy() {
    this.connection.unsubscribe();
  }
}
