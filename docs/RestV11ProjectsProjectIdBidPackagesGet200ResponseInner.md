# RestV11ProjectsProjectIdBidPackagesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**bid_due_date** | **datetime** | Due date | [optional] 
**number** | **int** | Package Number | [optional] 
**title** | **str** | Title | [optional] 
**submitted_bids_count** | **int** | Number bids submitted | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_bid_packages_get200_response_inner import RestV11ProjectsProjectIdBidPackagesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdBidPackagesGet200ResponseInner from a JSON string
rest_v11_projects_project_id_bid_packages_get200_response_inner_instance = RestV11ProjectsProjectIdBidPackagesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdBidPackagesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_bid_packages_get200_response_inner_dict = rest_v11_projects_project_id_bid_packages_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdBidPackagesGet200ResponseInner from a dict
rest_v11_projects_project_id_bid_packages_get200_response_inner_from_dict = RestV11ProjectsProjectIdBidPackagesGet200ResponseInner.from_dict(rest_v11_projects_project_id_bid_packages_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


