import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Message } from '../../models/message.model';
import { Headers, Http } from '@angular/http';

@Injectable()
export class ChatroomMessageListService {
  private messageList: Array<Message> = [];
  private URL = "http://localhost:8080/api/chat";
  constructor(private http:Http){}
  public getMessageList(): any {
    return this.messageList;
  }

  public addMessage(message: any): void {
    this.messageList.push(message);
  }

   retrieveMessageFromBot(userMessage:string){
     let params: URLSearchParams = new URLSearchParams();
     params.set('message', userMessage);
     let headers = new Headers();
     headers.append('Content-Type', 'application/json');

     //Http request-
     return this.http.get(this.URL, {
       search: params,
     }).map(res => res.json());
  }
}
