package libs
{
	public class NumberBreaker
	{
		private var valueNumber:Number = 0;
		private const MASTER_A:Number = 11;
		private const MASTER_B:Number = 22;
		//--
		private var isMasterResult:Boolean;
		private var masterResult:Number = 0;
		private var finalResult:Number = 0;
		
		public function NumberBreaker( val:Number )
		{
			valueNumber = val;
			init();
		}
		
		private function init():void
		{
			
			finalResult = valueCrusher(valueCrusher(valueNumber));
		}
		
		//-- getters
		public function get isMaster():Boolean
		{
			return isMasterResult;
		}
		
		public function get masterValue():Number
		{
			return masterResult;
		}
		
		public function get getfinalResult():Number
		{
			return finalResult;
		}
		
//--
		private function valueCrusher( numVal:Number ):Number
		{
			
			var loacalValue:Number = 0;
			if ( numVal == MASTER_A || numVal == MASTER_B )
			{
				isMasterResult = true;
				masterResult = numVal
				trace( "one master number" );
				loacalValue = masterResult;
			} else {
			var numValStr:String = String(numVal);
			var arrToCrush:Array = new Array();
			var accumullatedValue:Number = 0;
			arrToCrush = numValStr.split("");
			
			//--
			
			for (var i:Number = 0; i < arrToCrush.length; i+= 1){
				
				accumullatedValue += Number(arrToCrush[i]);
				
				if (i == (arrToCrush.length-1)){
			
					
				loacalValue = accumullatedValue;
				//-----
				}
				//--
				
				}
				
			}
			
			return loacalValue;
			
			
		}
		//--
	}
}