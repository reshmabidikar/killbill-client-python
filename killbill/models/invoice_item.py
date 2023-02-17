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



class InvoiceItem(object):
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
        'invoice_item_id': 'Str',
        'invoice_id': 'Str',
        'linked_invoice_item_id': 'Str',
        'account_id': 'Str',
        'child_account_id': 'Str',
        'bundle_id': 'Str',
        'subscription_id': 'Str',
        'product_name': 'Str',
        'plan_name': 'Str',
        'phase_name': 'Str',
        'usage_name': 'Str',
        'pretty_product_name': 'Str',
        'pretty_plan_name': 'Str',
        'pretty_phase_name': 'Str',
        'pretty_usage_name': 'Str',
        'item_type': 'Str',
        'description': 'Str',
        'start_date': 'Date',
        'end_date': 'Date',
        'amount': 'Float',
        'rate': 'Float',
        'currency': 'Str',
        'quantity': 'Float',
        'item_details': 'Str',
        'catalog_effective_date': 'Datetime',
        'child_items': 'List[InvoiceItem]',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'invoice_item_id': 'invoiceItemId',
        'invoice_id': 'invoiceId',
        'linked_invoice_item_id': 'linkedInvoiceItemId',
        'account_id': 'accountId',
        'child_account_id': 'childAccountId',
        'bundle_id': 'bundleId',
        'subscription_id': 'subscriptionId',
        'product_name': 'productName',
        'plan_name': 'planName',
        'phase_name': 'phaseName',
        'usage_name': 'usageName',
        'pretty_product_name': 'prettyProductName',
        'pretty_plan_name': 'prettyPlanName',
        'pretty_phase_name': 'prettyPhaseName',
        'pretty_usage_name': 'prettyUsageName',
        'item_type': 'itemType',
        'description': 'description',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'amount': 'amount',
        'rate': 'rate',
        'currency': 'currency',
        'quantity': 'quantity',
        'item_details': 'itemDetails',
        'catalog_effective_date': 'catalogEffectiveDate',
        'child_items': 'childItems',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, invoice_item_id=None, invoice_id=None, linked_invoice_item_id=None, account_id=None, child_account_id=None, bundle_id=None, subscription_id=None, product_name=None, plan_name=None, phase_name=None, usage_name=None, pretty_product_name=None, pretty_plan_name=None, pretty_phase_name=None, pretty_usage_name=None, item_type=None, description=None, start_date=None, end_date=None, amount=None, rate=None, currency=None, quantity=None, item_details=None, catalog_effective_date=None, child_items=None, audit_logs=None):  # noqa: E501
        """InvoiceItem - a model defined in Swagger"""  # noqa: E501

        self._invoice_item_id = None
        self._invoice_id = None
        self._linked_invoice_item_id = None
        self._account_id = None
        self._child_account_id = None
        self._bundle_id = None
        self._subscription_id = None
        self._product_name = None
        self._plan_name = None
        self._phase_name = None
        self._usage_name = None
        self._pretty_product_name = None
        self._pretty_plan_name = None
        self._pretty_phase_name = None
        self._pretty_usage_name = None
        self._item_type = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._amount = None
        self._rate = None
        self._currency = None
        self._quantity = None
        self._item_details = None
        self._catalog_effective_date = None
        self._child_items = None
        self._audit_logs = None
        self.discriminator = None

        self.invoice_item_id = invoice_item_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if linked_invoice_item_id is not None:
            self.linked_invoice_item_id = linked_invoice_item_id
        self.account_id = account_id
        if child_account_id is not None:
            self.child_account_id = child_account_id
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if product_name is not None:
            self.product_name = product_name
        if plan_name is not None:
            self.plan_name = plan_name
        if phase_name is not None:
            self.phase_name = phase_name
        if usage_name is not None:
            self.usage_name = usage_name
        if pretty_product_name is not None:
            self.pretty_product_name = pretty_product_name
        if pretty_plan_name is not None:
            self.pretty_plan_name = pretty_plan_name
        if pretty_phase_name is not None:
            self.pretty_phase_name = pretty_phase_name
        if pretty_usage_name is not None:
            self.pretty_usage_name = pretty_usage_name
        if item_type is not None:
            self.item_type = item_type
        if description is not None:
            self.description = description
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if amount is not None:
            self.amount = amount
        if rate is not None:
            self.rate = rate
        if currency is not None:
            self.currency = currency
        if quantity is not None:
            self.quantity = quantity
        if item_details is not None:
            self.item_details = item_details
        if catalog_effective_date is not None:
            self.catalog_effective_date = catalog_effective_date
        if child_items is not None:
            self.child_items = child_items
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def invoice_item_id(self):
        """Gets the invoice_item_id of this InvoiceItem.  # noqa: E501


        :return: The invoice_item_id of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, invoice_item_id):
        """Sets the invoice_item_id of this InvoiceItem.


        :param invoice_item_id: The invoice_item_id of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._invoice_item_id = invoice_item_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this InvoiceItem.  # noqa: E501


        :return: The invoice_id of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this InvoiceItem.


        :param invoice_id: The invoice_id of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._invoice_id = invoice_id

    @property
    def linked_invoice_item_id(self):
        """Gets the linked_invoice_item_id of this InvoiceItem.  # noqa: E501


        :return: The linked_invoice_item_id of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._linked_invoice_item_id

    @linked_invoice_item_id.setter
    def linked_invoice_item_id(self, linked_invoice_item_id):
        """Sets the linked_invoice_item_id of this InvoiceItem.


        :param linked_invoice_item_id: The linked_invoice_item_id of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._linked_invoice_item_id = linked_invoice_item_id

    @property
    def account_id(self):
        """Gets the account_id of this InvoiceItem.  # noqa: E501


        :return: The account_id of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InvoiceItem.


        :param account_id: The account_id of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._account_id = account_id

    @property
    def child_account_id(self):
        """Gets the child_account_id of this InvoiceItem.  # noqa: E501


        :return: The child_account_id of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._child_account_id

    @child_account_id.setter
    def child_account_id(self, child_account_id):
        """Sets the child_account_id of this InvoiceItem.


        :param child_account_id: The child_account_id of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._child_account_id = child_account_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this InvoiceItem.  # noqa: E501


        :return: The bundle_id of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this InvoiceItem.


        :param bundle_id: The bundle_id of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._bundle_id = bundle_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this InvoiceItem.  # noqa: E501


        :return: The subscription_id of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this InvoiceItem.


        :param subscription_id: The subscription_id of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._subscription_id = subscription_id

    @property
    def product_name(self):
        """Gets the product_name of this InvoiceItem.  # noqa: E501


        :return: The product_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this InvoiceItem.


        :param product_name: The product_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._product_name = product_name

    @property
    def plan_name(self):
        """Gets the plan_name of this InvoiceItem.  # noqa: E501


        :return: The plan_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this InvoiceItem.


        :param plan_name: The plan_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._plan_name = plan_name

    @property
    def phase_name(self):
        """Gets the phase_name of this InvoiceItem.  # noqa: E501


        :return: The phase_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._phase_name

    @phase_name.setter
    def phase_name(self, phase_name):
        """Sets the phase_name of this InvoiceItem.


        :param phase_name: The phase_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._phase_name = phase_name

    @property
    def usage_name(self):
        """Gets the usage_name of this InvoiceItem.  # noqa: E501


        :return: The usage_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._usage_name

    @usage_name.setter
    def usage_name(self, usage_name):
        """Sets the usage_name of this InvoiceItem.


        :param usage_name: The usage_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._usage_name = usage_name

    @property
    def pretty_product_name(self):
        """Gets the pretty_product_name of this InvoiceItem.  # noqa: E501


        :return: The pretty_product_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._pretty_product_name

    @pretty_product_name.setter
    def pretty_product_name(self, pretty_product_name):
        """Sets the pretty_product_name of this InvoiceItem.


        :param pretty_product_name: The pretty_product_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._pretty_product_name = pretty_product_name

    @property
    def pretty_plan_name(self):
        """Gets the pretty_plan_name of this InvoiceItem.  # noqa: E501


        :return: The pretty_plan_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._pretty_plan_name

    @pretty_plan_name.setter
    def pretty_plan_name(self, pretty_plan_name):
        """Sets the pretty_plan_name of this InvoiceItem.


        :param pretty_plan_name: The pretty_plan_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._pretty_plan_name = pretty_plan_name

    @property
    def pretty_phase_name(self):
        """Gets the pretty_phase_name of this InvoiceItem.  # noqa: E501


        :return: The pretty_phase_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._pretty_phase_name

    @pretty_phase_name.setter
    def pretty_phase_name(self, pretty_phase_name):
        """Sets the pretty_phase_name of this InvoiceItem.


        :param pretty_phase_name: The pretty_phase_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._pretty_phase_name = pretty_phase_name

    @property
    def pretty_usage_name(self):
        """Gets the pretty_usage_name of this InvoiceItem.  # noqa: E501


        :return: The pretty_usage_name of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._pretty_usage_name

    @pretty_usage_name.setter
    def pretty_usage_name(self, pretty_usage_name):
        """Sets the pretty_usage_name of this InvoiceItem.


        :param pretty_usage_name: The pretty_usage_name of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._pretty_usage_name = pretty_usage_name

    @property
    def item_type(self):
        """Gets the item_type of this InvoiceItem.  # noqa: E501


        :return: The item_type of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this InvoiceItem.


        :param item_type: The item_type of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._item_type = item_type

    @property
    def description(self):
        """Gets the description of this InvoiceItem.  # noqa: E501


        :return: The description of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvoiceItem.


        :param description: The description of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._description = description

    @property
    def start_date(self):
        """Gets the start_date of this InvoiceItem.  # noqa: E501


        :return: The start_date of this InvoiceItem.  # noqa: E501
        :rtype: Date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InvoiceItem.


        :param start_date: The start_date of this InvoiceItem.  # noqa: E501
        :type: Date
        """


        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this InvoiceItem.  # noqa: E501


        :return: The end_date of this InvoiceItem.  # noqa: E501
        :rtype: Date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this InvoiceItem.


        :param end_date: The end_date of this InvoiceItem.  # noqa: E501
        :type: Date
        """


        self._end_date = end_date

    @property
    def amount(self):
        """Gets the amount of this InvoiceItem.  # noqa: E501


        :return: The amount of this InvoiceItem.  # noqa: E501
        :rtype: Float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceItem.


        :param amount: The amount of this InvoiceItem.  # noqa: E501
        :type: Float
        """


        self._amount = amount

    @property
    def rate(self):
        """Gets the rate of this InvoiceItem.  # noqa: E501


        :return: The rate of this InvoiceItem.  # noqa: E501
        :rtype: Float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this InvoiceItem.


        :param rate: The rate of this InvoiceItem.  # noqa: E501
        :type: Float
        """


        self._rate = rate

    @property
    def currency(self):
        """Gets the currency of this InvoiceItem.  # noqa: E501


        :return: The currency of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceItem.


        :param currency: The currency of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._currency = currency

    @property
    def quantity(self):
        """Gets the quantity of this InvoiceItem.  # noqa: E501


        :return: The quantity of this InvoiceItem.  # noqa: E501
        :rtype: Float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InvoiceItem.


        :param quantity: The quantity of this InvoiceItem.  # noqa: E501
        :type: Float
        """


        self._quantity = quantity

    @property
    def item_details(self):
        """Gets the item_details of this InvoiceItem.  # noqa: E501


        :return: The item_details of this InvoiceItem.  # noqa: E501
        :rtype: Str
        """
        return self._item_details

    @item_details.setter
    def item_details(self, item_details):
        """Sets the item_details of this InvoiceItem.


        :param item_details: The item_details of this InvoiceItem.  # noqa: E501
        :type: Str
        """


        self._item_details = item_details

    @property
    def catalog_effective_date(self):
        """Gets the catalog_effective_date of this InvoiceItem.  # noqa: E501


        :return: The catalog_effective_date of this InvoiceItem.  # noqa: E501
        :rtype: Datetime
        """
        return self._catalog_effective_date

    @catalog_effective_date.setter
    def catalog_effective_date(self, catalog_effective_date):
        """Sets the catalog_effective_date of this InvoiceItem.


        :param catalog_effective_date: The catalog_effective_date of this InvoiceItem.  # noqa: E501
        :type: Datetime
        """


        self._catalog_effective_date = catalog_effective_date

    @property
    def child_items(self):
        """Gets the child_items of this InvoiceItem.  # noqa: E501


        :return: The child_items of this InvoiceItem.  # noqa: E501
        :rtype: List[InvoiceItem]
        """
        return self._child_items

    @child_items.setter
    def child_items(self, child_items):
        """Sets the child_items of this InvoiceItem.


        :param child_items: The child_items of this InvoiceItem.  # noqa: E501
        :type: List[InvoiceItem]
        """


        self._child_items = child_items

    @property
    def audit_logs(self):
        """Gets the audit_logs of this InvoiceItem.  # noqa: E501


        :return: The audit_logs of this InvoiceItem.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this InvoiceItem.


        :param audit_logs: The audit_logs of this InvoiceItem.  # noqa: E501
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
        if not isinstance(other, InvoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
