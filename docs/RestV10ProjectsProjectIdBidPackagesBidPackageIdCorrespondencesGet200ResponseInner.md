# RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bid_package_id** | **int** | Bid package ID | [optional] 
**bid_package_title** | **str** | Bid package title | [optional] 
**created_at** | **str** | Correspondence created-at | [optional] 
**subject** | **str** | Subject within Correspondence | [optional] 
**attachments** | [**List[CorrespondenceAttachmentsInner]**](CorrespondenceAttachmentsInner.md) |  | [optional] 
**message** | **str** | Body of Correspondence | [optional] 
**recipients** | **List[List[CorrespondenceRecipientsInnerInner]]** | List of recipient names Correspondence was sent to | [optional] 
**var_from** | [**CorrespondenceFrom**](CorrespondenceFrom.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner import RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner_instance = RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner_dict = rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner from a dict
rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner_from_dict = RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner.from_dict(rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


