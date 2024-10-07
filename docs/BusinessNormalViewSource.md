# BusinessNormalViewSource

Information about where the business information was sourced from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the business in the source data. For example, typeform id in snowflake | [optional] 
**source** | **str** | More detailed source information, for example the source field on snowflake records | [optional] 
**type** | **str** | The high level source this data was pulled from. This is currently always &#39;snowflake&#39; | [optional] 
**record_type** | **str** | More detailed type information, for example the record type on snowflake records | [optional] 

## Example

```python
from procore_sdk.models.business_normal_view_source import BusinessNormalViewSource

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessNormalViewSource from a JSON string
business_normal_view_source_instance = BusinessNormalViewSource.from_json(json)
# print the JSON string representation of the object
print(BusinessNormalViewSource.to_json())

# convert the object into a dict
business_normal_view_source_dict = business_normal_view_source_instance.to_dict()
# create an instance of BusinessNormalViewSource from a dict
business_normal_view_source_from_dict = BusinessNormalViewSource.from_dict(business_normal_view_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


