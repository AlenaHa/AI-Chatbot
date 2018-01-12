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
  private question: Message;
  private answer: Message;
  private textValue: string;
  private messageBot: Array<string>;

  ngOnInit() {
    this.messageListService.getMessageList();
  }

  constructor(private messageListService: ChatroomMessageListService){}

  ngOnChanges(): void {
    this.messageListService.getMessageList();
  }

  retrieveData(responseData : any){
      this.textValue = responseData.data;
  }

   showError() {
       console.log("Failed to retrieve data from server.")
   }
  public addMessage(): void {
    this.question = new Message(this.textValue, "user");
    this.textValue = "";
    this.messageListService.addMessage(this.question);
    this.messageListService.getMessageList();

    this.messageListService.retrieveMessageFromBot(this.question.text)
      .subscribe(
        (data) => this.retrieveData(data),
        (err) => this.showError());

    this.answer = new Message(this.textValue, "bot");
    this.messageListService.addMessage(this.answer);
    this.messageListService.getMessageList();
  }
}
