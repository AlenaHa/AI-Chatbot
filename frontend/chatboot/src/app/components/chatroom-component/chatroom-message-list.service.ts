import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class ChatroomMessageListService {
  private messageList: Array<any> = [];

  public getMessageList(): any {
    return this.messageList;
  }

  public addMessage(message: any): void {
    this.messageList.push(message);
  }
}
