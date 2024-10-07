# RestV10ProjectsProjectIdBidPackagesPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_post_due_submissions** | **bool** | Accepts bid post due submissions | [optional] 
**accounting_method** | **str** | Bid package accounting method, either &#39;amount&#39; or &#39;unit&#39; | [optional] 
**allow_bidder_sum** | **bool** | Allow lump sum bidding | [optional] 
**anticipated_award_date** | **date** | Anticipated award date | [optional] 
**bidding_countdown_email_days** | **int** | Days before sending countdown email | [optional] 
**bid_docs_manifest** | [**RestV10ProjectsProjectIdBidPackagesPost201ResponseBidDocsManifest**](RestV10ProjectsProjectIdBidPackagesPost201ResponseBidDocsManifest.md) |  | [optional] 
**bid_due_date** | **datetime** | Due date | [optional] 
**bid_email_message** | **str** | Information displayed in emails for Bidders | [optional] 
**bid_emails_include_link_to_bidding_documents** | **bool** | Include link to download zipped bidding documents in the Bid Invitation email | [optional] 
**bid_submission_confirmation** | **str** | Bid Package submission confirmation text | [optional] 
**bid_web_message** | **str** | Bid Package instructions for Bidder | [optional] 
**blind_bidding** | **bool** | Enable blind bidding | [optional] 
**created_by** | [**RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy**](RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy.md) |  | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdBidPackagesPost201ResponseDistributionMembersInner]**](RestV10ProjectsProjectIdBidPackagesPost201ResponseDistributionMembersInner.md) | Array of the distribution members | [optional] 
**distribution_member_ids** | **List[int]** | Array of distribution member ids | [optional] 
**enable_countdown_emails** | **bool** | Enable countdown emails | [optional] 
**enable_prebid_rfi_deadline** | **bool** | Enable prebid RFI deadline | [optional] 
**enable_prebid_walkthrough** | **bool** | Enable prebid walkthrough | [optional] 
**hidden** | **bool** | Whether or not the bid package has been recycled | [optional] 
**id** | **int** | ID | [optional] 
**links** | [**RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks**](RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks.md) |  | [optional] 
**lump_sum_bidding** | **bool** | Lump Sum Bidding Enabled | [optional] 
**manager** | [**RestV10ProjectsProjectIdBidPackagesPost201ResponseManager**](RestV10ProjectsProjectIdBidPackagesPost201ResponseManager.md) |  | [optional] 
**number** | **int** | Bid Package Number | [optional] 
**open** | **bool** | Whether or not the bid package is active | [optional] 
**point_of_contact** | [**RestV10ProjectsProjectIdBidPackagesPost201ResponsePointOfContact**](RestV10ProjectsProjectIdBidPackagesPost201ResponsePointOfContact.md) |  | [optional] 
**point_of_contact_login_id** | **int** | Point of contact ID | [optional] 
**pre_bid_rfi_deadline_date** | **datetime** | Prebid RFI deadline date | [optional] 
**pre_bid_walk_through_date** | **datetime** | Scheduled pre-bid walkthrough date | [optional] 
**pre_bid_walk_through_notes** | **str** | Pre-bid walkthrough notes | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**project_image_url** | **str** | Link to project image | [optional] 
**project_latitude** | **str** | Latitude of project location | [optional] 
**project_location** | **str** | Address of bid package project | [optional] 
**project_longitude** | **str** | Longtitude of project location | [optional] 
**project_name** | **str** | Name of bid package project | [optional] 
**sealed** | **bool** | Enabled sealed bidding | [optional] 
**show_bid_info** | **bool** | Show bid info | [optional] 
**submitted_bids_count** | **int** | Number bids submitted | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response import RestV10ProjectsProjectIdBidPackagesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBidPackagesPost201Response from a JSON string
rest_v10_projects_project_id_bid_packages_post201_response_instance = RestV10ProjectsProjectIdBidPackagesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBidPackagesPost201Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_bid_packages_post201_response_dict = rest_v10_projects_project_id_bid_packages_post201_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBidPackagesPost201Response from a dict
rest_v10_projects_project_id_bid_packages_post201_response_from_dict = RestV10ProjectsProjectIdBidPackagesPost201Response.from_dict(rest_v10_projects_project_id_bid_packages_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


