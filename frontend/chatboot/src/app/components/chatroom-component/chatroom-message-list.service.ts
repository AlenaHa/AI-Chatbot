import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Message } from '../../models/message.model';
import { Headers, Http } from '@angular/http';

@Injectable()
export class ChatroomMessageListService {
  private messageList: Array<Message> = [];

  public getMessageList(): any {
    return this.messageList;
  }

  public addMessage(message: any): void {
    this.messageList.push(message);
  }

}
