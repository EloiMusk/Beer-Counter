import { Component } from '@angular/core';
// @ts-ignore
import { NFC } from 'nfc-pcsc';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  nfc = new NFC

}
