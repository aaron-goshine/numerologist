package libs
{
	public class ValueSpliter
	{
		private var charListArr:Array;
		private var charListStr:String;
		private var namesArr:Array;
		private var whyPosArrObjs:Array = new Array();
		private var objItems:Object;
		
		public function ValueSpliter( valueList:String )
		{
			charListStr = valueList.toLowerCase();
			init();
		}
		
		//-- main function 
		private function init():void
		{
			charListArr = new Array();
			//--- spilitting  chars in to list 
			charListArr = spliter( charListStr );
			splitOnSpace( charListStr )
		}
		
		//-- getters 
		public function get getchars():Array
		{
			return charListArr;
		}
		
		public function get getNames():Array
		{
			return namesArr;
		}
		
		public function get getObjYs():Array
		{
			return whyPosArrObjs;
		}
		
		//-- function to split input into  an Array of characters
		private function spliter( charList:String ):Array
		{
			var listArr:Array = new Array();
			listArr = cleanCharList( charList ).split( "" );
			return listArr;
		}
		
		//--
		private function cleanCharList( charList:String ):String
		{
			var str:String = "";
			var myPattern:RegExp = /[^a-zA-Z]/gi;
			str = charList.replace( myPattern, "" );
			return str;
		}
		
		//--
		private function splitOnSpace( initStr:String ):void
		{
			var arr1:Array = new Array();
			//-- spilt initial word at spaces 
			arr1 = initStr.split( " " );
			//assign global value to array 
			namesArr = arr1;
			for ( var i:Number = 0; i < arr1.length; i += 1 )
			{
				var arr2:Array = new Array();
				var wordLen:Number = arr1[ i ].length;
				var currentWordPos:Number = i;
				//-- spilt individual word at chars
				arr2 = arr1[ i ].split( "" );
				//-- the current positon is = i
				//-- second inception
				for ( var j:Number = 0; j < arr2.length; j += 1 )
				{
					var currCharPos:Number = j;
					//trace( arr2[ j ]);
					if ( j <= ( arr2.length - 2 ) && j > 0 && arr2[ j ] == "y" )
					{
						//trace( "Why is vowel" );
						//-
						objItems = new Object();
						objItems.wordPos = new Number( currentWordPos );
						objItems.charPos = new Number( currCharPos );
						objItems.isVowel = new Boolean( true );
						whyPosArrObjs.push( objItems );
							//--
					}
					else if (( j == ( arr2.length - 1 ) && arr2[ j ] == "y" ) || ( j < 1 && arr2[ j ] == "y" ))
					{
						//trace( "Why not  vowel" );
						//-
						objItems = new Object();
						objItems.wordPos = new Number( currentWordPos );
						objItems.charPos = new Number( currCharPos );
						objItems.isVowel = new Boolean( false );
						whyPosArrObjs.push( objItems );
						//--
					}
				}
					//--
			}
			//---
		}
		
		//--
		private function implode( arrCol:Array ):String
		{
			var str:String = '';
			for ( var i:Number = 0; i < arrCol.length; i++ )
			{
				str += arrCol[ i ];
			}
			return str;
		}
		;
		// End Function
	}
}