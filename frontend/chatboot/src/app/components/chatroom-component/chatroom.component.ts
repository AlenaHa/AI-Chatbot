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

  constructor(private chatService: ChatService, private messageListService: ChatroomMessageListService) { }

  chat() {

    this.message = new Message(this.textValue, "user");
    this.chatService.sendMessage(this.message.text);
    this.messageListService.addMessage(this.message);
    this.messageListService.getMessageList();

    this.connection = this.chatService.getMessages().subscribe(msg => {
      var msgString = msg.toString();
      this.message = new Message(msgString, "bot");
    });
      this.messageListService.addMessage(this.message.text);
      this.messageListService.getMessageList();

  }

  ngOnChanges(): void {
      this.messageListService.getMessageList();
  }

  ngOnInit() {
     this.connection = this.chatService.connect();
  }

  ngOnDestroy() {
    this.connection.unsubscribe();
  }
}
