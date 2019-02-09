package libs
{
	import flash.display.Sprite;
	import flash.events.*;
	import flash.net.*;
	import flash.filesystem.File;
	public class DataLoader extends Sprite
	{
		private var xmlPath:String;
		private var selectedData:String;
		private var loader:URLLoader;
		private var urlReq:URLRequest;
		private var pureXml:XML = new XML();
		
		public function DataLoader( url:String )
		{
			
			
			var appDir:File = File.applicationDirectory;
			appDir;
			//	var appDir = "~/Documents/Adobe\ Flash\ Builder\ 4.5/NN"
			
			this.xmlPath = "../"+url;
			
			this.init();
		}
		
		private function init():void
		{
			
			this.loader = new URLLoader();
			this.urlReq = new URLRequest(xmlPath );
			this.loader.addEventListener( Event.COMPLETE, completeLoad );

		
			this.loader.load( this.urlReq );
		}
		
		public function get getDatavalue():XML
		{
			return this.pureXml;
		}
		
		private function completeLoad( event:Event ):void
		{
			
			this.pureXml = XML(event.target.data);
			dispatchEvent( new Event("ready"));
		}
	}
}