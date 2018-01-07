import { Component, OnChanges, OnInit } from '@angular/core';
import { MessageComponent } from '../message-component/message.component';
import { ChatroomMessageListService } from './chatroom-message-list.service';
import { Message } from '../../models/message.model';

@Component({
  selector: 'app-chatroom',
  templateUrl: './chatroom.component.html',
  styleUrls: ['./chatroom.component.scss'],
  providers: [ChatroomMessageListService]
})
export class ChatroomComponent implements OnChanges, OnInit{
  private message: Message;
  private textValue: string;
  private messageBot: Array<string> = ["Cum te numesti?", "Cati ani ai?", "Inteleg", "Cu ce te ocupi?"];
  
  ngOnInit() {
    this.message = new Message("Buna! Sunt bot","bot");
    this.messageListService.addMessage(this.message);
    this.messageListService.getMessageList();    
  }

  constructor(private messageListService: ChatroomMessageListService){}

  ngOnChanges(): void {
    this.messageListService.getMessageList();
  }

  public addMessage(): void {
    this.message = new Message(this.textValue,"human");    
    this.textValue = "";
    this.messageListService.addMessage(this.message);
    this.messageListService.getMessageList();   
    
    var rand = this.messageBot[Math.floor(Math.random() * this.messageBot.length)];
    this.message = new Message(rand,'bot');
    this.messageListService.addMessage(this.message);
    this.messageListService.getMessageList();  
  }
}
