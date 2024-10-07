# BusinessNormalViewCoverageAreasInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Country Code | [optional] 
**google_place_id** | **str** | Google Place ID | [optional] 
**admin1** | **str** | State (Province) | [optional] 
**admin2** | **str** | County | [optional] 
**admin3** | **str** | Not used in US | [optional] 
**admin4** | **str** | Not used in US | [optional] 
**locality** | **str** | Locality (City) | [optional] 
**selected_level** | **str** | The admin level that was originally chosen by user | [optional] 

## Example

```python
from procore_sdk.models.business_normal_view_coverage_areas_inner import BusinessNormalViewCoverageAreasInner

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessNormalViewCoverageAreasInner from a JSON string
business_normal_view_coverage_areas_inner_instance = BusinessNormalViewCoverageAreasInner.from_json(json)
# print the JSON string representation of the object
print(BusinessNormalViewCoverageAreasInner.to_json())

# convert the object into a dict
business_normal_view_coverage_areas_inner_dict = business_normal_view_coverage_areas_inner_instance.to_dict()
# create an instance of BusinessNormalViewCoverageAreasInner from a dict
business_normal_view_coverage_areas_inner_from_dict = BusinessNormalViewCoverageAreasInner.from_dict(business_normal_view_coverage_areas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


