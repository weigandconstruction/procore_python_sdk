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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_bid_docs_manifest import RestV10ProjectsProjectIdBidPackagesPost201ResponseBidDocsManifest
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_created_by import RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_distribution_members_inner import RestV10ProjectsProjectIdBidPackagesPost201ResponseDistributionMembersInner
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_links import RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_manager import RestV10ProjectsProjectIdBidPackagesPost201ResponseManager
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_point_of_contact import RestV10ProjectsProjectIdBidPackagesPost201ResponsePointOfContact
from typing import Optional, Set
from typing_extensions import Self

class RestV10ProjectsProjectIdBidPackagesPost201Response(BaseModel):
    """
    RestV10ProjectsProjectIdBidPackagesPost201Response
    """ # noqa: E501
    accept_post_due_submissions: Optional[StrictBool] = Field(default=None, description="Accepts bid post due submissions")
    accounting_method: Optional[StrictStr] = Field(default=None, description="Bid package accounting method, either 'amount' or 'unit'")
    allow_bidder_sum: Optional[StrictBool] = Field(default=None, description="Allow lump sum bidding")
    anticipated_award_date: Optional[date] = Field(default=None, description="Anticipated award date")
    bidding_countdown_email_days: Optional[StrictInt] = Field(default=None, description="Days before sending countdown email")
    bid_docs_manifest: Optional[RestV10ProjectsProjectIdBidPackagesPost201ResponseBidDocsManifest] = None
    bid_due_date: Optional[datetime] = Field(default=None, description="Due date")
    bid_email_message: Optional[StrictStr] = Field(default=None, description="Information displayed in emails for Bidders")
    bid_emails_include_link_to_bidding_documents: Optional[StrictBool] = Field(default=None, description="Include link to download zipped bidding documents in the Bid Invitation email")
    bid_submission_confirmation: Optional[StrictStr] = Field(default=None, description="Bid Package submission confirmation text")
    bid_web_message: Optional[StrictStr] = Field(default=None, description="Bid Package instructions for Bidder")
    blind_bidding: Optional[StrictBool] = Field(default=None, description="Enable blind bidding")
    created_by: Optional[RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy] = None
    distribution_members: Optional[List[RestV10ProjectsProjectIdBidPackagesPost201ResponseDistributionMembersInner]] = Field(default=None, description="Array of the distribution members")
    distribution_member_ids: Optional[List[StrictInt]] = Field(default=None, description="Array of distribution member ids")
    enable_countdown_emails: Optional[StrictBool] = Field(default=None, description="Enable countdown emails")
    enable_prebid_rfi_deadline: Optional[StrictBool] = Field(default=None, description="Enable prebid RFI deadline")
    enable_prebid_walkthrough: Optional[StrictBool] = Field(default=None, description="Enable prebid walkthrough")
    hidden: Optional[StrictBool] = Field(default=None, description="Whether or not the bid package has been recycled")
    id: Optional[StrictInt] = Field(default=None, description="ID")
    links: Optional[RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks] = None
    lump_sum_bidding: Optional[StrictBool] = Field(default=None, description="Lump Sum Bidding Enabled")
    manager: Optional[RestV10ProjectsProjectIdBidPackagesPost201ResponseManager] = None
    number: Optional[StrictInt] = Field(default=None, description="Bid Package Number")
    open: Optional[StrictBool] = Field(default=None, description="Whether or not the bid package is active")
    point_of_contact: Optional[RestV10ProjectsProjectIdBidPackagesPost201ResponsePointOfContact] = None
    point_of_contact_login_id: Optional[StrictInt] = Field(default=None, description="Point of contact ID")
    pre_bid_rfi_deadline_date: Optional[datetime] = Field(default=None, description="Prebid RFI deadline date")
    pre_bid_walk_through_date: Optional[datetime] = Field(default=None, description="Scheduled pre-bid walkthrough date")
    pre_bid_walk_through_notes: Optional[StrictStr] = Field(default=None, description="Pre-bid walkthrough notes")
    project_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the project.")
    project_image_url: Optional[StrictStr] = Field(default=None, description="Link to project image")
    project_latitude: Optional[StrictStr] = Field(default=None, description="Latitude of project location")
    project_location: Optional[StrictStr] = Field(default=None, description="Address of bid package project")
    project_longitude: Optional[StrictStr] = Field(default=None, description="Longtitude of project location")
    project_name: Optional[StrictStr] = Field(default=None, description="Name of bid package project")
    sealed: Optional[StrictBool] = Field(default=None, description="Enabled sealed bidding")
    show_bid_info: Optional[StrictBool] = Field(default=None, description="Show bid info")
    submitted_bids_count: Optional[StrictInt] = Field(default=None, description="Number bids submitted")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    __properties: ClassVar[List[str]] = ["accept_post_due_submissions", "accounting_method", "allow_bidder_sum", "anticipated_award_date", "bidding_countdown_email_days", "bid_docs_manifest", "bid_due_date", "bid_email_message", "bid_emails_include_link_to_bidding_documents", "bid_submission_confirmation", "bid_web_message", "blind_bidding", "created_by", "distribution_members", "distribution_member_ids", "enable_countdown_emails", "enable_prebid_rfi_deadline", "enable_prebid_walkthrough", "hidden", "id", "links", "lump_sum_bidding", "manager", "number", "open", "point_of_contact", "point_of_contact_login_id", "pre_bid_rfi_deadline_date", "pre_bid_walk_through_date", "pre_bid_walk_through_notes", "project_id", "project_image_url", "project_latitude", "project_location", "project_longitude", "project_name", "sealed", "show_bid_info", "submitted_bids_count", "title"]

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
        """Create an instance of RestV10ProjectsProjectIdBidPackagesPost201Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bid_docs_manifest
        if self.bid_docs_manifest:
            _dict['bid_docs_manifest'] = self.bid_docs_manifest.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in distribution_members (list)
        _items = []
        if self.distribution_members:
            for _item_distribution_members in self.distribution_members:
                if _item_distribution_members:
                    _items.append(_item_distribution_members.to_dict())
            _dict['distribution_members'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manager
        if self.manager:
            _dict['manager'] = self.manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of point_of_contact
        if self.point_of_contact:
            _dict['point_of_contact'] = self.point_of_contact.to_dict()
        # set to None if anticipated_award_date (nullable) is None
        # and model_fields_set contains the field
        if self.anticipated_award_date is None and "anticipated_award_date" in self.model_fields_set:
            _dict['anticipated_award_date'] = None

        # set to None if bidding_countdown_email_days (nullable) is None
        # and model_fields_set contains the field
        if self.bidding_countdown_email_days is None and "bidding_countdown_email_days" in self.model_fields_set:
            _dict['bidding_countdown_email_days'] = None

        # set to None if bid_docs_manifest (nullable) is None
        # and model_fields_set contains the field
        if self.bid_docs_manifest is None and "bid_docs_manifest" in self.model_fields_set:
            _dict['bid_docs_manifest'] = None

        # set to None if bid_submission_confirmation (nullable) is None
        # and model_fields_set contains the field
        if self.bid_submission_confirmation is None and "bid_submission_confirmation" in self.model_fields_set:
            _dict['bid_submission_confirmation'] = None

        # set to None if number (nullable) is None
        # and model_fields_set contains the field
        if self.number is None and "number" in self.model_fields_set:
            _dict['number'] = None

        # set to None if point_of_contact_login_id (nullable) is None
        # and model_fields_set contains the field
        if self.point_of_contact_login_id is None and "point_of_contact_login_id" in self.model_fields_set:
            _dict['point_of_contact_login_id'] = None

        # set to None if pre_bid_rfi_deadline_date (nullable) is None
        # and model_fields_set contains the field
        if self.pre_bid_rfi_deadline_date is None and "pre_bid_rfi_deadline_date" in self.model_fields_set:
            _dict['pre_bid_rfi_deadline_date'] = None

        # set to None if pre_bid_walk_through_date (nullable) is None
        # and model_fields_set contains the field
        if self.pre_bid_walk_through_date is None and "pre_bid_walk_through_date" in self.model_fields_set:
            _dict['pre_bid_walk_through_date'] = None

        # set to None if pre_bid_walk_through_notes (nullable) is None
        # and model_fields_set contains the field
        if self.pre_bid_walk_through_notes is None and "pre_bid_walk_through_notes" in self.model_fields_set:
            _dict['pre_bid_walk_through_notes'] = None

        # set to None if project_image_url (nullable) is None
        # and model_fields_set contains the field
        if self.project_image_url is None and "project_image_url" in self.model_fields_set:
            _dict['project_image_url'] = None

        # set to None if project_latitude (nullable) is None
        # and model_fields_set contains the field
        if self.project_latitude is None and "project_latitude" in self.model_fields_set:
            _dict['project_latitude'] = None

        # set to None if project_longitude (nullable) is None
        # and model_fields_set contains the field
        if self.project_longitude is None and "project_longitude" in self.model_fields_set:
            _dict['project_longitude'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestV10ProjectsProjectIdBidPackagesPost201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accept_post_due_submissions": obj.get("accept_post_due_submissions"),
            "accounting_method": obj.get("accounting_method"),
            "allow_bidder_sum": obj.get("allow_bidder_sum"),
            "anticipated_award_date": obj.get("anticipated_award_date"),
            "bidding_countdown_email_days": obj.get("bidding_countdown_email_days"),
            "bid_docs_manifest": RestV10ProjectsProjectIdBidPackagesPost201ResponseBidDocsManifest.from_dict(obj["bid_docs_manifest"]) if obj.get("bid_docs_manifest") is not None else None,
            "bid_due_date": obj.get("bid_due_date"),
            "bid_email_message": obj.get("bid_email_message"),
            "bid_emails_include_link_to_bidding_documents": obj.get("bid_emails_include_link_to_bidding_documents"),
            "bid_submission_confirmation": obj.get("bid_submission_confirmation"),
            "bid_web_message": obj.get("bid_web_message"),
            "blind_bidding": obj.get("blind_bidding"),
            "created_by": RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "distribution_members": [RestV10ProjectsProjectIdBidPackagesPost201ResponseDistributionMembersInner.from_dict(_item) for _item in obj["distribution_members"]] if obj.get("distribution_members") is not None else None,
            "distribution_member_ids": obj.get("distribution_member_ids"),
            "enable_countdown_emails": obj.get("enable_countdown_emails"),
            "enable_prebid_rfi_deadline": obj.get("enable_prebid_rfi_deadline"),
            "enable_prebid_walkthrough": obj.get("enable_prebid_walkthrough"),
            "hidden": obj.get("hidden"),
            "id": obj.get("id"),
            "links": RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "lump_sum_bidding": obj.get("lump_sum_bidding"),
            "manager": RestV10ProjectsProjectIdBidPackagesPost201ResponseManager.from_dict(obj["manager"]) if obj.get("manager") is not None else None,
            "number": obj.get("number"),
            "open": obj.get("open"),
            "point_of_contact": RestV10ProjectsProjectIdBidPackagesPost201ResponsePointOfContact.from_dict(obj["point_of_contact"]) if obj.get("point_of_contact") is not None else None,
            "point_of_contact_login_id": obj.get("point_of_contact_login_id"),
            "pre_bid_rfi_deadline_date": obj.get("pre_bid_rfi_deadline_date"),
            "pre_bid_walk_through_date": obj.get("pre_bid_walk_through_date"),
            "pre_bid_walk_through_notes": obj.get("pre_bid_walk_through_notes"),
            "project_id": obj.get("project_id"),
            "project_image_url": obj.get("project_image_url"),
            "project_latitude": obj.get("project_latitude"),
            "project_location": obj.get("project_location"),
            "project_longitude": obj.get("project_longitude"),
            "project_name": obj.get("project_name"),
            "sealed": obj.get("sealed"),
            "show_bid_info": obj.get("show_bid_info"),
            "submitted_bids_count": obj.get("submitted_bids_count"),
            "title": obj.get("title")
        })
        return _obj


