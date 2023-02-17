# coding: utf-8

#
# Copyright 2010-2014 Ning, Inc.
# Copyright 2014-2020 Groupon, Inc
# Copyright 2020-2021 Equinix, Inc
# Copyright 2014-2021 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.24.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class Invoice(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount': 'Float',
        'currency': 'Str',
        'status': 'Str',
        'credit_adj': 'Float',
        'refund_adj': 'Float',
        'invoice_id': 'Str',
        'invoice_date': 'Date',
        'target_date': 'Date',
        'invoice_number': 'Str',
        'balance': 'Float',
        'account_id': 'Str',
        'bundle_keys': 'Str',
        'credits': 'List[InvoiceItem]',
        'items': 'List[InvoiceItem]',
        'tracking_ids': 'List[Str]',
        'is_parent_invoice': 'Bool',
        'parent_invoice_id': 'Str',
        'parent_account_id': 'Str',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'status': 'status',
        'credit_adj': 'creditAdj',
        'refund_adj': 'refundAdj',
        'invoice_id': 'invoiceId',
        'invoice_date': 'invoiceDate',
        'target_date': 'targetDate',
        'invoice_number': 'invoiceNumber',
        'balance': 'balance',
        'account_id': 'accountId',
        'bundle_keys': 'bundleKeys',
        'credits': 'credits',
        'items': 'items',
        'tracking_ids': 'trackingIds',
        'is_parent_invoice': 'isParentInvoice',
        'parent_invoice_id': 'parentInvoiceId',
        'parent_account_id': 'parentAccountId',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, amount=None, currency=None, status=None, credit_adj=None, refund_adj=None, invoice_id=None, invoice_date=None, target_date=None, invoice_number=None, balance=None, account_id=None, bundle_keys=None, credits=None, items=None, tracking_ids=None, is_parent_invoice=None, parent_invoice_id=None, parent_account_id=None, audit_logs=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._currency = None
        self._status = None
        self._credit_adj = None
        self._refund_adj = None
        self._invoice_id = None
        self._invoice_date = None
        self._target_date = None
        self._invoice_number = None
        self._balance = None
        self._account_id = None
        self._bundle_keys = None
        self._credits = None
        self._items = None
        self._tracking_ids = None
        self._is_parent_invoice = None
        self._parent_invoice_id = None
        self._parent_account_id = None
        self._audit_logs = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if status is not None:
            self.status = status
        if credit_adj is not None:
            self.credit_adj = credit_adj
        if refund_adj is not None:
            self.refund_adj = refund_adj
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if target_date is not None:
            self.target_date = target_date
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if balance is not None:
            self.balance = balance
        if account_id is not None:
            self.account_id = account_id
        if bundle_keys is not None:
            self.bundle_keys = bundle_keys
        if credits is not None:
            self.credits = credits
        if items is not None:
            self.items = items
        if tracking_ids is not None:
            self.tracking_ids = tracking_ids
        if is_parent_invoice is not None:
            self.is_parent_invoice = is_parent_invoice
        if parent_invoice_id is not None:
            self.parent_invoice_id = parent_invoice_id
        if parent_account_id is not None:
            self.parent_account_id = parent_account_id
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def amount(self):
        """Gets the amount of this Invoice.  # noqa: E501


        :return: The amount of this Invoice.  # noqa: E501
        :rtype: Float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Invoice.


        :param amount: The amount of this Invoice.  # noqa: E501
        :type: Float
        """


        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Invoice.  # noqa: E501


        :return: The currency of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Invoice.


        :param currency: The currency of this Invoice.  # noqa: E501
        :type: Str
        """


        self._currency = currency

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501


        :return: The status of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.  # noqa: E501
        :type: Str
        """


        self._status = status

    @property
    def credit_adj(self):
        """Gets the credit_adj of this Invoice.  # noqa: E501


        :return: The credit_adj of this Invoice.  # noqa: E501
        :rtype: Float
        """
        return self._credit_adj

    @credit_adj.setter
    def credit_adj(self, credit_adj):
        """Sets the credit_adj of this Invoice.


        :param credit_adj: The credit_adj of this Invoice.  # noqa: E501
        :type: Float
        """


        self._credit_adj = credit_adj

    @property
    def refund_adj(self):
        """Gets the refund_adj of this Invoice.  # noqa: E501


        :return: The refund_adj of this Invoice.  # noqa: E501
        :rtype: Float
        """
        return self._refund_adj

    @refund_adj.setter
    def refund_adj(self, refund_adj):
        """Sets the refund_adj of this Invoice.


        :param refund_adj: The refund_adj of this Invoice.  # noqa: E501
        :type: Float
        """


        self._refund_adj = refund_adj

    @property
    def invoice_id(self):
        """Gets the invoice_id of this Invoice.  # noqa: E501


        :return: The invoice_id of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this Invoice.


        :param invoice_id: The invoice_id of this Invoice.  # noqa: E501
        :type: Str
        """


        self._invoice_id = invoice_id

    @property
    def invoice_date(self):
        """Gets the invoice_date of this Invoice.  # noqa: E501


        :return: The invoice_date of this Invoice.  # noqa: E501
        :rtype: Date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this Invoice.


        :param invoice_date: The invoice_date of this Invoice.  # noqa: E501
        :type: Date
        """


        self._invoice_date = invoice_date

    @property
    def target_date(self):
        """Gets the target_date of this Invoice.  # noqa: E501


        :return: The target_date of this Invoice.  # noqa: E501
        :rtype: Date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this Invoice.


        :param target_date: The target_date of this Invoice.  # noqa: E501
        :type: Date
        """


        self._target_date = target_date

    @property
    def invoice_number(self):
        """Gets the invoice_number of this Invoice.  # noqa: E501


        :return: The invoice_number of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this Invoice.


        :param invoice_number: The invoice_number of this Invoice.  # noqa: E501
        :type: Str
        """


        self._invoice_number = invoice_number

    @property
    def balance(self):
        """Gets the balance of this Invoice.  # noqa: E501


        :return: The balance of this Invoice.  # noqa: E501
        :rtype: Float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Invoice.


        :param balance: The balance of this Invoice.  # noqa: E501
        :type: Float
        """


        self._balance = balance

    @property
    def account_id(self):
        """Gets the account_id of this Invoice.  # noqa: E501


        :return: The account_id of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Invoice.


        :param account_id: The account_id of this Invoice.  # noqa: E501
        :type: Str
        """


        self._account_id = account_id

    @property
    def bundle_keys(self):
        """Gets the bundle_keys of this Invoice.  # noqa: E501


        :return: The bundle_keys of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._bundle_keys

    @bundle_keys.setter
    def bundle_keys(self, bundle_keys):
        """Sets the bundle_keys of this Invoice.


        :param bundle_keys: The bundle_keys of this Invoice.  # noqa: E501
        :type: Str
        """


        self._bundle_keys = bundle_keys

    @property
    def credits(self):
        """Gets the credits of this Invoice.  # noqa: E501


        :return: The credits of this Invoice.  # noqa: E501
        :rtype: List[InvoiceItem]
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """Sets the credits of this Invoice.


        :param credits: The credits of this Invoice.  # noqa: E501
        :type: List[InvoiceItem]
        """


        self._credits = credits

    @property
    def items(self):
        """Gets the items of this Invoice.  # noqa: E501


        :return: The items of this Invoice.  # noqa: E501
        :rtype: List[InvoiceItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Invoice.


        :param items: The items of this Invoice.  # noqa: E501
        :type: List[InvoiceItem]
        """


        self._items = items

    @property
    def tracking_ids(self):
        """Gets the tracking_ids of this Invoice.  # noqa: E501


        :return: The tracking_ids of this Invoice.  # noqa: E501
        :rtype: List[Str]
        """
        return self._tracking_ids

    @tracking_ids.setter
    def tracking_ids(self, tracking_ids):
        """Sets the tracking_ids of this Invoice.


        :param tracking_ids: The tracking_ids of this Invoice.  # noqa: E501
        :type: List[Str]
        """


        self._tracking_ids = tracking_ids

    @property
    def is_parent_invoice(self):
        """Gets the is_parent_invoice of this Invoice.  # noqa: E501


        :return: The is_parent_invoice of this Invoice.  # noqa: E501
        :rtype: Bool
        """
        return self._is_parent_invoice

    @is_parent_invoice.setter
    def is_parent_invoice(self, is_parent_invoice):
        """Sets the is_parent_invoice of this Invoice.


        :param is_parent_invoice: The is_parent_invoice of this Invoice.  # noqa: E501
        :type: Bool
        """


        self._is_parent_invoice = is_parent_invoice

    @property
    def parent_invoice_id(self):
        """Gets the parent_invoice_id of this Invoice.  # noqa: E501


        :return: The parent_invoice_id of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._parent_invoice_id

    @parent_invoice_id.setter
    def parent_invoice_id(self, parent_invoice_id):
        """Sets the parent_invoice_id of this Invoice.


        :param parent_invoice_id: The parent_invoice_id of this Invoice.  # noqa: E501
        :type: Str
        """


        self._parent_invoice_id = parent_invoice_id

    @property
    def parent_account_id(self):
        """Gets the parent_account_id of this Invoice.  # noqa: E501


        :return: The parent_account_id of this Invoice.  # noqa: E501
        :rtype: Str
        """
        return self._parent_account_id

    @parent_account_id.setter
    def parent_account_id(self, parent_account_id):
        """Sets the parent_account_id of this Invoice.


        :param parent_account_id: The parent_account_id of this Invoice.  # noqa: E501
        :type: Str
        """


        self._parent_account_id = parent_account_id

    @property
    def audit_logs(self):
        """Gets the audit_logs of this Invoice.  # noqa: E501


        :return: The audit_logs of this Invoice.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this Invoice.


        :param audit_logs: The audit_logs of this Invoice.  # noqa: E501
        :type: List[AuditLog]
        """


        self._audit_logs = audit_logs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
