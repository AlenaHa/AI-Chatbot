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

  private
  connection;
  message:Message;

  constructor(private chatService: ChatService, private messageListService: ChatroomMessageListService) { }

  chat() {
    this.message.user = 'user'
    this.chatService.sendMessage(this.message.text);
    this.message.text = '';
    this.messageListService.addMessage(this.message);
    this.messageListService.getMessageList();

   this.connection = this.chatService.getMessages().subscribe(message => {
    this.message.user ="bot";
    this.messageListService.addMessage(message);
    this.messageListService.getMessageList();
    });
  }

  ngOnChanges(): void {
    this.messageListService.getMessageList();
  }

  ngOnInit() {
    this.connection = this.chatService.getMessages().subscribe(message => {
    this.message.user ="bot";
    this.messageListService.addMessage(message);
    this.messageListService.getMessageList();
    });
  }

  ngOnDestroy() {
    this.connection.unsubscribe();
  }
}
