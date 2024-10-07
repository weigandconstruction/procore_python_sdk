# RestV10CompaniesCompanyIdBidsGet200ResponseInner

Summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bid_package_id** | **int** | Bid Package ID | [optional] 
**bid_package_title** | **str** | Bid Package title | [optional] 
**bid_form_title** | **str** | Bid Form Title | [optional] 
**bid_status** | **str** | Bid status | [optional] 
**awarded** | **bool** | Bid awarded to vendor | [optional] 
**company_id** | **int** | Company ID | [optional] 
**invitation_last_sent_at** | **datetime** | Date/time the Bid Package invitation was last sent | [optional] 
**is_bidder_committed** | **bool** | Bidder committed | [optional] 
**lump_sum_amount** | **float** | Lump sum (overall) amount | [optional] 
**lump_sum_enabled** | **bool** | Lump sum bidding enabled | [optional] 
**submitted** | **bool** | Vendor submitted Bid | [optional] 
**created_at** | **datetime** | Date/time the Bid Package was created | [optional] 
**updated_at** | **datetime** | Date/time the Bid Package was last updated | [optional] 
**due_date** | **datetime** | Due Date | [optional] 
**bidder_comments** | **str** | Comments | [optional] 
**bid_requester** | [**BidBidRequester**](BidBidRequester.md) |  | [optional] 
**vendor** | [**BidVendor**](BidVendor.md) |  | [optional] 
**project** | [**BidProject**](BidProject.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bids_get200_response_inner import RestV10CompaniesCompanyIdBidsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_bids_get200_response_inner_instance = RestV10CompaniesCompanyIdBidsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bids_get200_response_inner_dict = rest_v10_companies_company_id_bids_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidsGet200ResponseInner from a dict
rest_v10_companies_company_id_bids_get200_response_inner_from_dict = RestV10CompaniesCompanyIdBidsGet200ResponseInner.from_dict(rest_v10_companies_company_id_bids_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


