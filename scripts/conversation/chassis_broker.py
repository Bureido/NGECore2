from resources.common import ConversationOption
from resources.common import OutOfBand
from resources.common import ProsePackage
from resources.common import RadialOptions
from services.sui import SUIWindow
from services.sui.SUIWindow import Trigger
from java.util import Vector
from main import NGECore
import sys

def startConversation(core, actor, npc):
	convSvc = core.conversationService
	
	convSvc.sendConversationMessage(actor, npc, OutOfBand.ProsePackage('@conversation/chassis_npc:s_9ed93871'))
	
	options = Vector()
	options.add(ConversationOption(OutOfBand.ProsePackage('@conversation/chassis_npc:s_2f553ea8'), 0))
	options.add(ConversationOption(OutOfBand.ProsePackage('@conversation/chassis_npc:s_94e3013f'), 1))
	options.add(ConversationOption(OutOfBand.ProsePackage('@conversation/chassis_npc:s_93a92e8'), 2))
	options.add(ConversationOption(OutOfBand.ProsePackage('@conversation/chassis_npc:s_42d3759c'), 3))
	convSvc.sendConversationOptions(actor, npc, options, handleFirstScreen)
	
	return
	
def handleFirstScreen(core, actor, npc, selection):
	convSvc = core.conversationService
	
	if selection == 0:
		convSvc.sendStopConversation(actor, npc, 'conversation/chassis_npc','s_bcb592f')
		startConversation(core, actor, npc)
		return
			
	if selection == 1:
	#sell items
		sellItemListRef = core.lootService.getSellableInventoryItems(actor)
		if len(sellItemListRef) == 0:
			actor.sendSystemMessage()
			startConversation(core, actor, npc)
			convSvc.sendStopConversation(actor, npc, 'conversation/chassis_npc','s_3310c404')
			return
			
		convSvc.sendStopConversation(actor, npc, 'conversation/chassis_npc', 's_aa81853')
		core.lootService.handleJunkDealerSellWindow(actor, npc, sellItemListRef)
		return
		#JunkDealerSellerWIndow to be changed
				
	
	if selection == 2:
	#how do I assemble
		convSvc.sendStopConversation(actor, npc,'conversation/chassis_npc','s_37386aa2')
		return
	
	if selection == 3:
	#come back later
		convSvc.sendStopConversation(actor, npc, 'conversation/chassis_npc', 's_37f48153')
		return
		
def endConversation(core, actor, npc):
	core.conversationService.sendStopConversation(actor, npc, 'conversation/chassis_npc', 's_37f48153')
	return 
		
