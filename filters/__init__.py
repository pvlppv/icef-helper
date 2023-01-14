from aiogram import Dispatcher

from .IsDataBaseUserMessage import IsDatabaseUserMessage, IsDatabaseUserCallback
from .IsPrivateMessage import IsPrivateMessage, IsPrivateCallback
from .IsGroupMessage import IsSUPERGROUPMessage, IsSUPERGROUPCallback
# from .IsSubscriptionUserAddedNoErrorPleaseMessage import IsSubscriptionUserAddedNoErrorPleaseMessage, IsSubscriptionUserAddedNoErrorPleaseCallback
# from .IsSubscriptionUserMessage import IsSubscriptionUserMessage, IsSubscriptionUserCallback
from .IsAcceptedUserMessage import IsAcceptedUserMessage, IsAccepterUserCallback
from .IsSubscriberChannel import IsSubscriberChannelMessage, IsSubscriberChannelCallback


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivateMessage)
    dp.filters_factory.bind(IsPrivateCallback)
    dp.filters_factory.bind(IsDatabaseUserMessage)
    dp.filters_factory.bind(IsDatabaseUserCallback)
    dp.filters_factory.bind(IsSUPERGROUPMessage)
    dp.filters_factory.bind(IsSUPERGROUPCallback)
    # dp.filters_factory.bind(IsSubscriptionUserMessage)
    # dp.filters_factory.bind(IsSubscriptionUserCallback)
    # dp.filters_factory.bind(IsSubscriptionUserAddedNoErrorPleaseMessage)
    # dp.filters_factory.bind(IsSubscriptionUserAddedNoErrorPleaseCallback)
    dp.filters_factory.bind(IsAcceptedUserMessage)
    dp.filters_factory.bind(IsAccepterUserCallback)
    dp.filters_factory.bind(IsSubscriberChannelMessage)
    dp.filters_factory.bind(IsSubscriberChannelCallback)




