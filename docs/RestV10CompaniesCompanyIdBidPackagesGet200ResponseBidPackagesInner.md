# RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**bid_due_date** | **datetime** | Due date | [optional] 
**number** | **int** | Bid Package Number | [optional] 
**title** | **str** | Title | [optional] 
**project_name** | **str** | Name of bid package project | [optional] 
**project_location** | **str** | Address of bid package project | [optional] 
**accounting_method** | **str** | Bid package accounting method, either &#39;amount&#39; or &#39;unit&#39; | [optional] 
**formatted_bid_due_date** | **str** | This is the date at which bids are due for this bid package | [optional] 
**links** | [**RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInnerLinks**](RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInnerLinks.md) |  | [optional] 
**allow_bidder_sum** | **bool** | TODO | [optional] 
**accept_post_due_submissions** | **bool** |  | [optional] 
**sealed** | **bool** |  | [optional] 
**bid_invites_sent_count** | **float** |  | [optional] 
**bids_received_count** | **float** |  | [optional] 
**enable_prebid_walkthrough** | **bool** |  | [optional] 
**enable_prebid_rfi_deadline** | **bool** |  | [optional] 
**pre_bid_rfi_deadline_date** | **str** |  | [optional] 
**formatted_bid_web_message** | **str** |  | [optional] 
**formatted_bid_email_message** | **str** |  | [optional] 
**formatted_pre_bid_walk_through_notes** | **str** |  | [optional] 
**has_bid_docs** | **bool** |  | [optional] 
**user_bid_id** | **int** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bid_packages_get200_response_bid_packages_inner import RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInner from a JSON string
rest_v10_companies_company_id_bid_packages_get200_response_bid_packages_inner_instance = RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bid_packages_get200_response_bid_packages_inner_dict = rest_v10_companies_company_id_bid_packages_get200_response_bid_packages_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInner from a dict
rest_v10_companies_company_id_bid_packages_get200_response_bid_packages_inner_from_dict = RestV10CompaniesCompanyIdBidPackagesGet200ResponseBidPackagesInner.from_dict(rest_v10_companies_company_id_bid_packages_get200_response_bid_packages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


