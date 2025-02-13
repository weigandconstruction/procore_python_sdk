# coding: utf-8

"""
    Procore Rest API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Contact: apisupport@procore.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.normal_view_attachments_inner import NormalViewAttachmentsInner
from procore_sdk.models.normal_view_business_register import NormalViewBusinessRegister
from procore_sdk.models.normal_view_primary_contact import NormalViewPrimaryContact
from procore_sdk.models.normal_view_vendor_group import NormalViewVendorGroup
from procore_sdk.models.rest_v10_projects_project_id_vendors_inactive_get200_response_inner_all_of_links import RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInnerAllOfLinks
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner(BaseModel):
    """
    RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    abbreviated_name: Optional[StrictStr] = Field(default=None, description="Abbreviated name")
    address: Optional[StrictStr] = Field(default=None, description="Address")
    attachments: Optional[List[NormalViewAttachmentsInner]] = Field(default=None, description="Attachments")
    authorized_bidder: Optional[StrictBool] = Field(default=None, description="Authorized bidder status")
    business_id: Optional[StrictStr] = Field(default=None, description="Business id")
    business_phone: Optional[StrictStr] = Field(default=None, description="Business phone")
    business_register: Optional[NormalViewBusinessRegister] = None
    city: Optional[StrictStr] = Field(default=None, description="City")
    company: Optional[StrictStr] = Field(default=None, description="Company")
    company_vendor: Optional[StrictBool] = Field(default=None, description="Denotes whether this is the Company's Vendor")
    contact_count: Optional[StrictInt] = Field(default=None, description="Count of active Contacts associated with the vendor record")
    country_code: Optional[StrictStr] = Field(default=None, description="Country code (ISO-3166 Alpha-2 format)")
    created_at: Optional[datetime] = Field(default=None, description="Created at")
    email_address: Optional[StrictStr] = Field(default=None, description="Email address")
    fax_number: Optional[StrictStr] = Field(default=None, description="Fax number")
    is_active: Optional[StrictBool] = Field(default=None, description="Active status")
    is_connected: Optional[StrictBool] = Field(default=None, description="Connected status")
    labor_union: Optional[StrictStr] = Field(default=None, description="Labor union")
    license_number: Optional[StrictStr] = Field(default=None, description="License number")
    logo: Optional[StrictStr] = Field(default=None, description="Logo url")
    mobile_phone: Optional[StrictStr] = Field(default=None, description="Mobile phone")
    non_union_prevailing_wage: Optional[StrictBool] = Field(default=None, description="Non union prevailing wage status")
    notes: Optional[StrictStr] = Field(default=None, description="Notes")
    origin_code: Optional[StrictStr] = Field(default=None, description="Origin Code")
    origin_data: Optional[StrictStr] = Field(default=None, description="Origin data")
    origin_id: Optional[StrictStr] = Field(default=None, description="Origin ID")
    prequalified: Optional[StrictBool] = Field(default=None, description="Prequalified status")
    primary_contact: Optional[NormalViewPrimaryContact] = None
    state_code: Optional[StrictStr] = Field(default=None, description="State code (ISO-3166 Alpha-2 format)")
    synced_to_erp: Optional[StrictBool] = Field(default=None, description="Synced to ERP")
    trade_name: Optional[StrictStr] = Field(default=None, description="Vendor's Trade Name, also known as Doing Business As (DBA).")
    union_member: Optional[StrictBool] = Field(default=None, description="Union member status")
    updated_at: Optional[datetime] = Field(default=None, description="Updated at")
    vendor_group: Optional[NormalViewVendorGroup] = None
    website: Optional[StrictStr] = Field(default=None, description="Website url")
    zip: Optional[StrictStr] = Field(default=None, description="Zip code")
    links: Optional[RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInnerAllOfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["id", "name", "abbreviated_name", "address", "attachments", "authorized_bidder", "business_id", "business_phone", "business_register", "city", "company", "company_vendor", "contact_count", "country_code", "created_at", "email_address", "fax_number", "is_active", "is_connected", "labor_union", "license_number", "logo", "mobile_phone", "non_union_prevailing_wage", "notes", "origin_code", "origin_data", "origin_id", "prequalified", "primary_contact", "state_code", "synced_to_erp", "trade_name", "union_member", "updated_at", "vendor_group", "website", "zip", "_links"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of business_register
        if self.business_register:
            _dict['business_register'] = self.business_register.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_contact
        if self.primary_contact:
            _dict['primary_contact'] = self.primary_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor_group
        if self.vendor_group:
            _dict['vendor_group'] = self.vendor_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # set to None if abbreviated_name (nullable) is None
        # and model_fields_set contains the field
        if self.abbreviated_name is None and "abbreviated_name" in self.model_fields_set:
            _dict['abbreviated_name'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if business_id (nullable) is None
        # and model_fields_set contains the field
        if self.business_id is None and "business_id" in self.model_fields_set:
            _dict['business_id'] = None

        # set to None if business_phone (nullable) is None
        # and model_fields_set contains the field
        if self.business_phone is None and "business_phone" in self.model_fields_set:
            _dict['business_phone'] = None

        # set to None if business_register (nullable) is None
        # and model_fields_set contains the field
        if self.business_register is None and "business_register" in self.model_fields_set:
            _dict['business_register'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if company (nullable) is None
        # and model_fields_set contains the field
        if self.company is None and "company" in self.model_fields_set:
            _dict['company'] = None

        # set to None if country_code (nullable) is None
        # and model_fields_set contains the field
        if self.country_code is None and "country_code" in self.model_fields_set:
            _dict['country_code'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if email_address (nullable) is None
        # and model_fields_set contains the field
        if self.email_address is None and "email_address" in self.model_fields_set:
            _dict['email_address'] = None

        # set to None if fax_number (nullable) is None
        # and model_fields_set contains the field
        if self.fax_number is None and "fax_number" in self.model_fields_set:
            _dict['fax_number'] = None

        # set to None if labor_union (nullable) is None
        # and model_fields_set contains the field
        if self.labor_union is None and "labor_union" in self.model_fields_set:
            _dict['labor_union'] = None

        # set to None if license_number (nullable) is None
        # and model_fields_set contains the field
        if self.license_number is None and "license_number" in self.model_fields_set:
            _dict['license_number'] = None

        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        # set to None if mobile_phone (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone is None and "mobile_phone" in self.model_fields_set:
            _dict['mobile_phone'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if origin_code (nullable) is None
        # and model_fields_set contains the field
        if self.origin_code is None and "origin_code" in self.model_fields_set:
            _dict['origin_code'] = None

        # set to None if origin_data (nullable) is None
        # and model_fields_set contains the field
        if self.origin_data is None and "origin_data" in self.model_fields_set:
            _dict['origin_data'] = None

        # set to None if origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_id is None and "origin_id" in self.model_fields_set:
            _dict['origin_id'] = None

        # set to None if primary_contact (nullable) is None
        # and model_fields_set contains the field
        if self.primary_contact is None and "primary_contact" in self.model_fields_set:
            _dict['primary_contact'] = None

        # set to None if state_code (nullable) is None
        # and model_fields_set contains the field
        if self.state_code is None and "state_code" in self.model_fields_set:
            _dict['state_code'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if vendor_group (nullable) is None
        # and model_fields_set contains the field
        if self.vendor_group is None and "vendor_group" in self.model_fields_set:
            _dict['vendor_group'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

        # set to None if zip (nullable) is None
        # and model_fields_set contains the field
        if self.zip is None and "zip" in self.model_fields_set:
            _dict['zip'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "abbreviated_name": obj.get("abbreviated_name"),
            "address": obj.get("address"),
            "attachments": [NormalViewAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "authorized_bidder": obj.get("authorized_bidder"),
            "business_id": obj.get("business_id"),
            "business_phone": obj.get("business_phone"),
            "business_register": NormalViewBusinessRegister.from_dict(obj["business_register"]) if obj.get("business_register") is not None else None,
            "city": obj.get("city"),
            "company": obj.get("company"),
            "company_vendor": obj.get("company_vendor"),
            "contact_count": obj.get("contact_count"),
            "country_code": obj.get("country_code"),
            "created_at": obj.get("created_at"),
            "email_address": obj.get("email_address"),
            "fax_number": obj.get("fax_number"),
            "is_active": obj.get("is_active"),
            "is_connected": obj.get("is_connected"),
            "labor_union": obj.get("labor_union"),
            "license_number": obj.get("license_number"),
            "logo": obj.get("logo"),
            "mobile_phone": obj.get("mobile_phone"),
            "non_union_prevailing_wage": obj.get("non_union_prevailing_wage"),
            "notes": obj.get("notes"),
            "origin_code": obj.get("origin_code"),
            "origin_data": obj.get("origin_data"),
            "origin_id": obj.get("origin_id"),
            "prequalified": obj.get("prequalified"),
            "primary_contact": NormalViewPrimaryContact.from_dict(obj["primary_contact"]) if obj.get("primary_contact") is not None else None,
            "state_code": obj.get("state_code"),
            "synced_to_erp": obj.get("synced_to_erp"),
            "trade_name": obj.get("trade_name"),
            "union_member": obj.get("union_member"),
            "updated_at": obj.get("updated_at"),
            "vendor_group": NormalViewVendorGroup.from_dict(obj["vendor_group"]) if obj.get("vendor_group") is not None else None,
            "website": obj.get("website"),
            "zip": obj.get("zip"),
            "_links": RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInnerAllOfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


