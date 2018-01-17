import { Observable } from 'rxjs/Observable';

import * as io from 'socket.io-client';

export class ChatService {
  private url = 'http://localhost:8080';
  private socket;

  sendMessage(message) {
    this.socket.emit('chat', message);
    console.log("MESSAGE SENT");
  }

  getMessages() {
    let observable = new Observable(observer => {
      this.socket = io(this.url);
      this.socket.on('chat', (data) => {
        observer.next(data);
      });
      return () => {
        this.socket.disconnect();
      }
    })

    return observable;
  }
}
